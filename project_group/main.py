import coh, overheads, profit_loss

def main():
    overhead_num = overheads.overheads()
    coh_num = coh.coh()
    profitloss_num = profit_loss.profitloss()

    with open("summary_report.txt","w") as file:
        file.write(f"{overhead_num}\n{coh_num}{profitloss_num}")

main()