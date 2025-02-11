import { connectToDatabase } from "../utils/db";

export default defineEventHandler(async () => {
    try {
        const { hotels } = await connectToDatabase();
        return await hotels.find().toArray();
    } catch (error) {
        console.error("Error fetching hotels:", error);
        return { error: "Failed to fetch hotels" };
    }
});
