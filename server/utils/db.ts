import { MongoClient, Db, Collection } from "mongodb";

const mongoUri = process.env.MONGO_URI || "mongodb://localhost:27017";
const dbName = process.env.DB_NAME || "Booking";

let client: MongoClient;
let db: Db;

export interface Restaurant {
    name: string;
    location: string;
    cuisine: string;
}

export interface Hotel {
    name: string;
    stars: number;
    city: string;
}

export interface Transport {
    type: string;
    company: string;
    capacity: number;
}

export async function connectToDatabase() {
    if (!client) {
        client = new MongoClient(mongoUri);
        await client.connect();
        console.log("✅ Connected to MongoDB!");
        db = client.db(dbName);
    }

    return {
        restaurants: db.collection<Restaurant>("restaurants"),
        hotels: db.collection<Hotel>("hotels"),
        transports: db.collection<Transport>("transports"),
    };
}
