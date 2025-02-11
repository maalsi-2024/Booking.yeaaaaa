import { connectToDatabase } from "../utils/db";

export default defineEventHandler(async () => {
    const { transports } = await connectToDatabase();
    return await transports.find().toArray();
});
