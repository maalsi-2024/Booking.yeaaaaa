import { connectToDatabase } from "../utils/db";

export default defineEventHandler(async () => {
    const { restaurants } = await connectToDatabase();
    return await restaurants.find().toArray();
});
