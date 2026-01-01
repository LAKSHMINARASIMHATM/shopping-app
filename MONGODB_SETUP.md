# MongoDB Connection Setup Guide

## Quick Setup

### Step 1: Create your `.env` file

In the `backend` directory, create a file named `.env` (without the .example extension) with the following content:

```env
# MongoDB Configuration
MONGO_URL=mongodb+srv://simha:narasimha@cluster0.nmaqxhm.mongodb.net/?appName=Cluster0
DB_NAME=shop_assistant

# JWT Secret (IMPORTANT: Change this to a random string!)
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production

# Google Gemini API (Required for AI features)
GEMINI_API_KEY=your-gemini-api-key-here

# OAuth Configuration (Optional - for Google/GitHub login)
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GITHUB_CLIENT_ID=
GITHUB_CLIENT_SECRET=

# Affiliate IDs (Optional - for price comparison links)
AMAZON_AFFILIATE_TAG=
FLIPKART_AFFILIATE_ID=
MEESHO_AFFILIATE_ID=
```

### Step 2: Verify MongoDB Connection

Your MongoDB connection string is:
```
mongodb+srv://simha:narasimha@cluster0.nmaqxhm.mongodb.net/?appName=Cluster0
```

**Important Notes:**
- Username: `simha`
- Password: `narasimha`
- Cluster: `cluster0.nmaqxhm.mongodb.net`
- Database: `shop_assistant` (will be created automatically)

### Step 3: Test the Connection

Run the backend server to test the connection:

```bash
cd backend
python -m uvicorn server:app --reload
```

If successful, you should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 4: Verify Database Collections

Once the server is running, the following collections will be created automatically when you use the app:
- `users` - User accounts and authentication
- `bills` - Uploaded bills and OCR data
- `shopping_lists` - Generated shopping lists

## MongoDB Atlas Configuration (Optional)

If you need to configure your MongoDB Atlas cluster:

1. **Whitelist IP Address:**
   - Go to MongoDB Atlas Dashboard
   - Navigate to Network Access
   - Add your IP address or use `0.0.0.0/0` for development (allow all)

2. **Database User:**
   - Verify user `simha` exists with password `narasimha`
   - Ensure user has read/write permissions

3. **Connection String:**
   - Your current connection string is correct
   - The database name `shop_assistant` will be created automatically

## Troubleshooting

### Connection Timeout
If you get a timeout error:
- Check your IP is whitelisted in MongoDB Atlas Network Access
- Verify your internet connection
- Check if MongoDB Atlas is accessible from your network

### Authentication Failed
If you get authentication errors:
- Verify username is `simha`
- Verify password is `narasimha`
- Check user permissions in MongoDB Atlas

### Database Not Found
This is normal! The database `shop_assistant` will be created automatically when you first insert data.

## Required Environment Variables

### Essential (Must Configure):
- `MONGO_URL` - Your MongoDB connection string ✅ (Already configured)
- `DB_NAME` - Database name ✅ (Set to `shop_assistant`)
- `JWT_SECRET` - Secret key for JWT tokens (change the default!)
- `GEMINI_API_KEY` - Google Gemini API key for AI features

### Optional:
- OAuth credentials (for social login)
- Affiliate IDs (for monetization)

## Next Steps

1. Create the `.env` file with your MongoDB credentials
2. Get a Google Gemini API key from: https://makersuite.google.com/app/apikey
3. Update the `JWT_SECRET` to a random secure string
4. Start the backend server
5. Test the API endpoints

## API Endpoints

Once running, you can access:
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/api/health (if available)
- Register User: http://localhost:8000/api/auth/register
