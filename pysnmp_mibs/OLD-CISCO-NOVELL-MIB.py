_G='ipxCkactDst'
_F='ipxCkactSrc'
_E='ipxActDst'
_D='ipxActSrc'
_C='OLD-CISCO-NOVELL-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
temporary,=mibBuilder.importSymbols('CISCO-SMI','temporary')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class IPXaddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Tmpnovell_ObjectIdentity=ObjectIdentity
tmpnovell=_Tmpnovell_ObjectIdentity((1,3,6,1,4,1,9,3,4))
_NovellInput_Type=Integer32
_NovellInput_Object=MibScalar
novellInput=_NovellInput_Object((1,3,6,1,4,1,9,3,4,1),_NovellInput_Type())
novellInput.setMaxAccess(_B)
if mibBuilder.loadTexts:novellInput.setStatus(_A)
_NovellBcastin_Type=Integer32
_NovellBcastin_Object=MibScalar
novellBcastin=_NovellBcastin_Object((1,3,6,1,4,1,9,3,4,2),_NovellBcastin_Type())
novellBcastin.setMaxAccess(_B)
if mibBuilder.loadTexts:novellBcastin.setStatus(_A)
_NovellForward_Type=Integer32
_NovellForward_Object=MibScalar
novellForward=_NovellForward_Object((1,3,6,1,4,1,9,3,4,3),_NovellForward_Type())
novellForward.setMaxAccess(_B)
if mibBuilder.loadTexts:novellForward.setStatus(_A)
_NovellBcastout_Type=Integer32
_NovellBcastout_Object=MibScalar
novellBcastout=_NovellBcastout_Object((1,3,6,1,4,1,9,3,4,4),_NovellBcastout_Type())
novellBcastout.setMaxAccess(_B)
if mibBuilder.loadTexts:novellBcastout.setStatus(_A)
_NovellFormerr_Type=Integer32
_NovellFormerr_Object=MibScalar
novellFormerr=_NovellFormerr_Object((1,3,6,1,4,1,9,3,4,5),_NovellFormerr_Type())
novellFormerr.setMaxAccess(_B)
if mibBuilder.loadTexts:novellFormerr.setStatus(_A)
_NovellChksum_Type=Integer32
_NovellChksum_Object=MibScalar
novellChksum=_NovellChksum_Object((1,3,6,1,4,1,9,3,4,6),_NovellChksum_Type())
novellChksum.setMaxAccess(_B)
if mibBuilder.loadTexts:novellChksum.setStatus(_A)
_NovellHopcnt_Type=Integer32
_NovellHopcnt_Object=MibScalar
novellHopcnt=_NovellHopcnt_Object((1,3,6,1,4,1,9,3,4,7),_NovellHopcnt_Type())
novellHopcnt.setMaxAccess(_B)
if mibBuilder.loadTexts:novellHopcnt.setStatus(_A)
_NovellNoroute_Type=Integer32
_NovellNoroute_Object=MibScalar
novellNoroute=_NovellNoroute_Object((1,3,6,1,4,1,9,3,4,8),_NovellNoroute_Type())
novellNoroute.setMaxAccess(_B)
if mibBuilder.loadTexts:novellNoroute.setStatus(_A)
_NovellNoencap_Type=Integer32
_NovellNoencap_Object=MibScalar
novellNoencap=_NovellNoencap_Object((1,3,6,1,4,1,9,3,4,9),_NovellNoencap_Type())
novellNoencap.setMaxAccess(_B)
if mibBuilder.loadTexts:novellNoencap.setStatus(_A)
_NovellOutput_Type=Integer32
_NovellOutput_Object=MibScalar
novellOutput=_NovellOutput_Object((1,3,6,1,4,1,9,3,4,10),_NovellOutput_Type())
novellOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:novellOutput.setStatus(_A)
_NovellInmult_Type=Integer32
_NovellInmult_Object=MibScalar
novellInmult=_NovellInmult_Object((1,3,6,1,4,1,9,3,4,11),_NovellInmult_Type())
novellInmult.setMaxAccess(_B)
if mibBuilder.loadTexts:novellInmult.setStatus(_A)
_NovellLocal_Type=Integer32
_NovellLocal_Object=MibScalar
novellLocal=_NovellLocal_Object((1,3,6,1,4,1,9,3,4,12),_NovellLocal_Type())
novellLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:novellLocal.setStatus(_A)
_NovellUnknown_Type=Integer32
_NovellUnknown_Object=MibScalar
novellUnknown=_NovellUnknown_Object((1,3,6,1,4,1,9,3,4,13),_NovellUnknown_Type())
novellUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:novellUnknown.setStatus(_A)
_NovellSapreqin_Type=Integer32
_NovellSapreqin_Object=MibScalar
novellSapreqin=_NovellSapreqin_Object((1,3,6,1,4,1,9,3,4,14),_NovellSapreqin_Type())
novellSapreqin.setMaxAccess(_B)
if mibBuilder.loadTexts:novellSapreqin.setStatus(_A)
_NovellSapresin_Type=Integer32
_NovellSapresin_Object=MibScalar
novellSapresin=_NovellSapresin_Object((1,3,6,1,4,1,9,3,4,15),_NovellSapresin_Type())
novellSapresin.setMaxAccess(_B)
if mibBuilder.loadTexts:novellSapresin.setStatus(_A)
_NovellSapout_Type=Integer32
_NovellSapout_Object=MibScalar
novellSapout=_NovellSapout_Object((1,3,6,1,4,1,9,3,4,16),_NovellSapout_Type())
novellSapout.setMaxAccess(_B)
if mibBuilder.loadTexts:novellSapout.setStatus(_A)
_NovellSapreply_Type=Integer32
_NovellSapreply_Object=MibScalar
novellSapreply=_NovellSapreply_Object((1,3,6,1,4,1,9,3,4,17),_NovellSapreply_Type())
novellSapreply.setMaxAccess(_B)
if mibBuilder.loadTexts:novellSapreply.setStatus(_A)
_IpxActThresh_Type=Integer32
_IpxActThresh_Object=MibScalar
ipxActThresh=_IpxActThresh_Object((1,3,6,1,4,1,9,3,4,18),_IpxActThresh_Type())
ipxActThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxActThresh.setStatus(_A)
_IpxActLostPkts_Type=Integer32
_IpxActLostPkts_Object=MibScalar
ipxActLostPkts=_IpxActLostPkts_Object((1,3,6,1,4,1,9,3,4,19),_IpxActLostPkts_Type())
ipxActLostPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxActLostPkts.setStatus(_A)
_IpxActLostByts_Type=Integer32
_IpxActLostByts_Object=MibScalar
ipxActLostByts=_IpxActLostByts_Object((1,3,6,1,4,1,9,3,4,20),_IpxActLostByts_Type())
ipxActLostByts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxActLostByts.setStatus(_A)
_LipxAccountingTable_Object=MibTable
lipxAccountingTable=_LipxAccountingTable_Object((1,3,6,1,4,1,9,3,4,21))
if mibBuilder.loadTexts:lipxAccountingTable.setStatus(_A)
_LipxAccountingEntry_Object=MibTableRow
lipxAccountingEntry=_LipxAccountingEntry_Object((1,3,6,1,4,1,9,3,4,21,1))
lipxAccountingEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:lipxAccountingEntry.setStatus(_A)
_IpxActSrc_Type=IPXaddress
_IpxActSrc_Object=MibTableColumn
ipxActSrc=_IpxActSrc_Object((1,3,6,1,4,1,9,3,4,21,1,1),_IpxActSrc_Type())
ipxActSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxActSrc.setStatus(_A)
_IpxActDst_Type=IPXaddress
_IpxActDst_Object=MibTableColumn
ipxActDst=_IpxActDst_Object((1,3,6,1,4,1,9,3,4,21,1,2),_IpxActDst_Type())
ipxActDst.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxActDst.setStatus(_A)
_IpxActPkts_Type=Integer32
_IpxActPkts_Object=MibTableColumn
ipxActPkts=_IpxActPkts_Object((1,3,6,1,4,1,9,3,4,21,1,3),_IpxActPkts_Type())
ipxActPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxActPkts.setStatus(_A)
_IpxActByts_Type=Integer32
_IpxActByts_Object=MibTableColumn
ipxActByts=_IpxActByts_Object((1,3,6,1,4,1,9,3,4,21,1,4),_IpxActByts_Type())
ipxActByts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxActByts.setStatus(_A)
_IpxActAge_Type=TimeTicks
_IpxActAge_Object=MibScalar
ipxActAge=_IpxActAge_Object((1,3,6,1,4,1,9,3,4,22),_IpxActAge_Type())
ipxActAge.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxActAge.setStatus(_A)
_LipxCkAccountingTable_Object=MibTable
lipxCkAccountingTable=_LipxCkAccountingTable_Object((1,3,6,1,4,1,9,3,4,23))
if mibBuilder.loadTexts:lipxCkAccountingTable.setStatus(_A)
_LipxCkAccountingEntry_Object=MibTableRow
lipxCkAccountingEntry=_LipxCkAccountingEntry_Object((1,3,6,1,4,1,9,3,4,23,1))
lipxCkAccountingEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:lipxCkAccountingEntry.setStatus(_A)
_IpxCkactSrc_Type=IPXaddress
_IpxCkactSrc_Object=MibTableColumn
ipxCkactSrc=_IpxCkactSrc_Object((1,3,6,1,4,1,9,3,4,23,1,1),_IpxCkactSrc_Type())
ipxCkactSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCkactSrc.setStatus(_A)
_IpxCkactDst_Type=IPXaddress
_IpxCkactDst_Object=MibTableColumn
ipxCkactDst=_IpxCkactDst_Object((1,3,6,1,4,1,9,3,4,23,1,2),_IpxCkactDst_Type())
ipxCkactDst.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCkactDst.setStatus(_A)
_IpxCkactPkts_Type=Integer32
_IpxCkactPkts_Object=MibTableColumn
ipxCkactPkts=_IpxCkactPkts_Object((1,3,6,1,4,1,9,3,4,23,1,3),_IpxCkactPkts_Type())
ipxCkactPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCkactPkts.setStatus(_A)
_IpxCkactByts_Type=Counter32
_IpxCkactByts_Object=MibTableColumn
ipxCkactByts=_IpxCkactByts_Object((1,3,6,1,4,1,9,3,4,23,1,4),_IpxCkactByts_Type())
ipxCkactByts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCkactByts.setStatus(_A)
_IpxCkactAge_Type=TimeTicks
_IpxCkactAge_Object=MibScalar
ipxCkactAge=_IpxCkactAge_Object((1,3,6,1,4,1,9,3,4,24),_IpxCkactAge_Type())
ipxCkactAge.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCkactAge.setStatus(_A)
_IpxActCheckPoint_Type=Integer32
_IpxActCheckPoint_Object=MibScalar
ipxActCheckPoint=_IpxActCheckPoint_Object((1,3,6,1,4,1,9,3,4,25),_IpxActCheckPoint_Type())
ipxActCheckPoint.setMaxAccess('read-write')
if mibBuilder.loadTexts:ipxActCheckPoint.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'IPXaddress':IPXaddress,'tmpnovell':tmpnovell,'novellInput':novellInput,'novellBcastin':novellBcastin,'novellForward':novellForward,'novellBcastout':novellBcastout,'novellFormerr':novellFormerr,'novellChksum':novellChksum,'novellHopcnt':novellHopcnt,'novellNoroute':novellNoroute,'novellNoencap':novellNoencap,'novellOutput':novellOutput,'novellInmult':novellInmult,'novellLocal':novellLocal,'novellUnknown':novellUnknown,'novellSapreqin':novellSapreqin,'novellSapresin':novellSapresin,'novellSapout':novellSapout,'novellSapreply':novellSapreply,'ipxActThresh':ipxActThresh,'ipxActLostPkts':ipxActLostPkts,'ipxActLostByts':ipxActLostByts,'lipxAccountingTable':lipxAccountingTable,'lipxAccountingEntry':lipxAccountingEntry,_D:ipxActSrc,_E:ipxActDst,'ipxActPkts':ipxActPkts,'ipxActByts':ipxActByts,'ipxActAge':ipxActAge,'lipxCkAccountingTable':lipxCkAccountingTable,'lipxCkAccountingEntry':lipxCkAccountingEntry,_F:ipxCkactSrc,_G:ipxCkactDst,'ipxCkactPkts':ipxCkactPkts,'ipxCkactByts':ipxCkactByts,'ipxCkactAge':ipxCkactAge,'ipxActCheckPoint':ipxActCheckPoint})