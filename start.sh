apt update && apt upgrade -y
apt install git -y       
pip install -U pip
git pull

git clone https://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@github.com/kidungamani/UserBot3 userbot3 
cd userbot3
python3 -m venv project-env
source project-env/bin/activate
pip install -U -r requirements.txt

# Install pm2 globally
apt install npm -y
npm install pm2 -g

# Start & Save pm2
pm2 start "python bot.py" --name userbot3
pm2 save
