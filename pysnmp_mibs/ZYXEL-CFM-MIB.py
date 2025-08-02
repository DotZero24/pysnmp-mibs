_G='Unsigned32'
_F='dot1agCfmMepIdentifier'
_E='dot1agCfmMdIndex'
_D='dot1agCfmMaIndex'
_C='IEEE8021-CFM-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1agCfmMaIndex,dot1agCfmMdIndex,dot1agCfmMepIdentifier=mibBuilder.importSymbols(_C,_D,_E,_F)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TDomain,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TDomain','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelCfm=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,13))
_ZyxelCfmSetup_ObjectIdentity=ObjectIdentity
zyxelCfmSetup=_ZyxelCfmSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,13,1))
_ZyCfmState_Type=EnabledStatus
_ZyCfmState_Object=MibScalar
zyCfmState=_ZyCfmState_Object((1,3,6,1,4,1,890,1,15,3,13,1,1),_ZyCfmState_Type())
zyCfmState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCfmState.setStatus(_A)
_ZyxelCfmMibObjects_ObjectIdentity=ObjectIdentity
zyxelCfmMibObjects=_ZyxelCfmMibObjects_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,13,1,2))
_ZyCfmMgmtIpAddressDomain_Type=TDomain
_ZyCfmMgmtIpAddressDomain_Object=MibScalar
zyCfmMgmtIpAddressDomain=_ZyCfmMgmtIpAddressDomain_Object((1,3,6,1,4,1,890,1,15,3,13,1,2,1),_ZyCfmMgmtIpAddressDomain_Type())
zyCfmMgmtIpAddressDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCfmMgmtIpAddressDomain.setStatus(_A)
_ZyCfmMgmtIpAddress_Type=IpAddress
_ZyCfmMgmtIpAddress_Object=MibScalar
zyCfmMgmtIpAddress=_ZyCfmMgmtIpAddress_Object((1,3,6,1,4,1,890,1,15,3,13,1,2,2),_ZyCfmMgmtIpAddress_Type())
zyCfmMgmtIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCfmMgmtIpAddress.setStatus(_A)
_ZyxelCfmMepTable_Object=MibTable
zyxelCfmMepTable=_ZyxelCfmMepTable_Object((1,3,6,1,4,1,890,1,15,3,13,1,2,3))
if mibBuilder.loadTexts:zyxelCfmMepTable.setStatus(_A)
_ZyxelCfmMepEntry_Object=MibTableRow
zyxelCfmMepEntry=_ZyxelCfmMepEntry_Object((1,3,6,1,4,1,890,1,15,3,13,1,2,3,1))
zyxelCfmMepEntry.setIndexNames((0,_C,_E),(0,_C,_D),(0,_C,_F))
if mibBuilder.loadTexts:zyxelCfmMepEntry.setStatus(_A)
class _ZyCfmMepTransmitLbmDataTlvSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1500))
_ZyCfmMepTransmitLbmDataTlvSize_Type.__name__=_G
_ZyCfmMepTransmitLbmDataTlvSize_Object=MibTableColumn
zyCfmMepTransmitLbmDataTlvSize=_ZyCfmMepTransmitLbmDataTlvSize_Object((1,3,6,1,4,1,890,1,15,3,13,1,2,3,1,1),_ZyCfmMepTransmitLbmDataTlvSize_Type())
zyCfmMepTransmitLbmDataTlvSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCfmMepTransmitLbmDataTlvSize.setStatus(_A)
_ZyxelCfmStatus_ObjectIdentity=ObjectIdentity
zyxelCfmStatus=_ZyxelCfmStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,13,2))
_ZyCfmLinkTraceClear_Type=EnabledStatus
_ZyCfmLinkTraceClear_Object=MibScalar
zyCfmLinkTraceClear=_ZyCfmLinkTraceClear_Object((1,3,6,1,4,1,890,1,15,3,13,2,1),_ZyCfmLinkTraceClear_Type())
zyCfmLinkTraceClear.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCfmLinkTraceClear.setStatus(_A)
_ZyCfmMepCcmDbClear_Type=EnabledStatus
_ZyCfmMepCcmDbClear_Object=MibScalar
zyCfmMepCcmDbClear=_ZyCfmMepCcmDbClear_Object((1,3,6,1,4,1,890,1,15,3,13,2,2),_ZyCfmMepCcmDbClear_Type())
zyCfmMepCcmDbClear.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCfmMepCcmDbClear.setStatus(_A)
_ZyCfmMepDefectsClear_Type=EnabledStatus
_ZyCfmMepDefectsClear_Object=MibScalar
zyCfmMepDefectsClear=_ZyCfmMepDefectsClear_Object((1,3,6,1,4,1,890,1,15,3,13,2,3),_ZyCfmMepDefectsClear_Type())
zyCfmMepDefectsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCfmMepDefectsClear.setStatus(_A)
_ZyCfmMipCcmDbClear_Type=EnabledStatus
_ZyCfmMipCcmDbClear_Object=MibScalar
zyCfmMipCcmDbClear=_ZyCfmMipCcmDbClear_Object((1,3,6,1,4,1,890,1,15,3,13,2,4),_ZyCfmMipCcmDbClear_Type())
zyCfmMipCcmDbClear.setMaxAccess(_B)
if mibBuilder.loadTexts:zyCfmMipCcmDbClear.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-CFM-MIB',**{'zyxelCfm':zyxelCfm,'zyxelCfmSetup':zyxelCfmSetup,'zyCfmState':zyCfmState,'zyxelCfmMibObjects':zyxelCfmMibObjects,'zyCfmMgmtIpAddressDomain':zyCfmMgmtIpAddressDomain,'zyCfmMgmtIpAddress':zyCfmMgmtIpAddress,'zyxelCfmMepTable':zyxelCfmMepTable,'zyxelCfmMepEntry':zyxelCfmMepEntry,'zyCfmMepTransmitLbmDataTlvSize':zyCfmMepTransmitLbmDataTlvSize,'zyxelCfmStatus':zyxelCfmStatus,'zyCfmLinkTraceClear':zyCfmLinkTraceClear,'zyCfmMepCcmDbClear':zyCfmMepCcmDbClear,'zyCfmMepDefectsClear':zyCfmMepDefectsClear,'zyCfmMipCcmDbClear':zyCfmMipCcmDbClear})