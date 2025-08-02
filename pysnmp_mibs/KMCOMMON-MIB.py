_b='kmMFPDocProcessorIndex'
_a='micrometers'
_Z='tenThousandthsOfInches'
_Y='kmMediaIndex'
_X='kmGroupMediaKindIndex'
_W='kmGroupIndex'
_V='locked'
_U='active'
_T='kmCounterSetItemIndex'
_S='kmCounterSetIndex'
_R='japanMetric'
_Q='asiaPacific'
_P='europeMetric'
_O='inch'
_N='notInstalled'
_M='kmColorModeIndex'
_L='OctetString'
_K='optional'
_J='write-only'
_I='not-accessible'
_H='KMCOMMON-MIB'
_G='DisplayString'
_F='hrDeviceIndex'
_E='HOST-RESOURCES-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hrDeviceIndex,=mibBuilder.importSymbols(_E,_F)
PresentOnOff,prtMarkerIndex=mibBuilder.importSymbols('Printer-MIB','PresentOnOff','prtMarkerIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Kyocera_ObjectIdentity=ObjectIdentity
kyocera=_Kyocera_ObjectIdentity((1,3,6,1,4,1,1347))
_KmCommon_ObjectIdentity=ObjectIdentity
kmCommon=_KmCommon_ObjectIdentity((1,3,6,1,4,1,1347,42))
_KmAccounting_ObjectIdentity=ObjectIdentity
kmAccounting=_KmAccounting_ObjectIdentity((1,3,6,1,4,1,1347,42,1))
_KmCounterSet_ObjectIdentity=ObjectIdentity
kmCounterSet=_KmCounterSet_ObjectIdentity((1,3,6,1,4,1,1347,42,1,1))
_KmCounterSetTable_Object=MibTable
kmCounterSetTable=_KmCounterSetTable_Object((1,3,6,1,4,1,1347,42,1,1,1))
if mibBuilder.loadTexts:kmCounterSetTable.setStatus(_A)
_KmCounterSetEntry_Object=MibTableRow
kmCounterSetEntry=_KmCounterSetEntry_Object((1,3,6,1,4,1,1347,42,1,1,1,1))
kmCounterSetEntry.setIndexNames((0,_E,_F),(0,_H,_S),(0,_H,_T))
if mibBuilder.loadTexts:kmCounterSetEntry.setStatus(_A)
_KmCounterSetIndex_Type=Integer32
_KmCounterSetIndex_Object=MibTableColumn
kmCounterSetIndex=_KmCounterSetIndex_Object((1,3,6,1,4,1,1347,42,1,1,1,1,1),_KmCounterSetIndex_Type())
kmCounterSetIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kmCounterSetIndex.setStatus(_A)
_KmCounterSetItemIndex_Type=Integer32
_KmCounterSetItemIndex_Object=MibTableColumn
kmCounterSetItemIndex=_KmCounterSetItemIndex_Object((1,3,6,1,4,1,1347,42,1,1,1,1,2),_KmCounterSetItemIndex_Type())
kmCounterSetItemIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kmCounterSetItemIndex.setStatus(_A)
_KmCounterItem_Type=Integer32
_KmCounterItem_Object=MibTableColumn
kmCounterItem=_KmCounterItem_Object((1,3,6,1,4,1,1347,42,1,1,1,1,3),_KmCounterItem_Type())
kmCounterItem.setMaxAccess(_B)
if mibBuilder.loadTexts:kmCounterItem.setStatus(_A)
_KmCounterMediaRef_Type=Integer32
_KmCounterMediaRef_Object=MibTableColumn
kmCounterMediaRef=_KmCounterMediaRef_Object((1,3,6,1,4,1,1347,42,1,1,1,1,4),_KmCounterMediaRef_Type())
kmCounterMediaRef.setMaxAccess(_B)
if mibBuilder.loadTexts:kmCounterMediaRef.setStatus(_A)
_KmCounterColorModeRef_Type=Integer32
_KmCounterColorModeRef_Object=MibTableColumn
kmCounterColorModeRef=_KmCounterColorModeRef_Object((1,3,6,1,4,1,1347,42,1,1,1,1,5),_KmCounterColorModeRef_Type())
kmCounterColorModeRef.setMaxAccess(_B)
if mibBuilder.loadTexts:kmCounterColorModeRef.setStatus(_A)
_KmAccountBalanceItem_Type=Integer32
_KmAccountBalanceItem_Object=MibTableColumn
kmAccountBalanceItem=_KmAccountBalanceItem_Object((1,3,6,1,4,1,1347,42,1,1,1,1,6),_KmAccountBalanceItem_Type())
kmAccountBalanceItem.setMaxAccess(_C)
if mibBuilder.loadTexts:kmAccountBalanceItem.setStatus(_K)
class _KmAccountBalanceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_KmAccountBalanceStatus_Type.__name__=_D
_KmAccountBalanceStatus_Object=MibTableColumn
kmAccountBalanceStatus=_KmAccountBalanceStatus_Object((1,3,6,1,4,1,1347,42,1,1,1,1,7),_KmAccountBalanceStatus_Type())
kmAccountBalanceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:kmAccountBalanceStatus.setStatus(_K)
class _KmAccountRestriction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_KmAccountRestriction_Type.__name__=_D
_KmAccountRestriction_Object=MibTableColumn
kmAccountRestriction=_KmAccountRestriction_Object((1,3,6,1,4,1,1347,42,1,1,1,1,8),_KmAccountRestriction_Type())
kmAccountRestriction.setMaxAccess(_C)
if mibBuilder.loadTexts:kmAccountRestriction.setStatus(_K)
_KmGroup_ObjectIdentity=ObjectIdentity
kmGroup=_KmGroup_ObjectIdentity((1,3,6,1,4,1,1347,42,1,2))
_KmGroupLevel1_ObjectIdentity=ObjectIdentity
kmGroupLevel1=_KmGroupLevel1_ObjectIdentity((1,3,6,1,4,1,1347,42,1,2,1))
_KmGroupConfigTable_Object=MibTable
kmGroupConfigTable=_KmGroupConfigTable_Object((1,3,6,1,4,1,1347,42,1,2,1,1))
if mibBuilder.loadTexts:kmGroupConfigTable.setStatus(_A)
_KmGroupConfigEntry_Object=MibTableRow
kmGroupConfigEntry=_KmGroupConfigEntry_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1))
kmGroupConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:kmGroupConfigEntry.setStatus(_A)
_KmGroupCodeWidth_Type=Integer32
_KmGroupCodeWidth_Object=MibTableColumn
kmGroupCodeWidth=_KmGroupCodeWidth_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,1),_KmGroupCodeWidth_Type())
kmGroupCodeWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupCodeWidth.setStatus(_A)
class _KmGroupSecurityLock_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_KmGroupSecurityLock_Type.__name__=_G
_KmGroupSecurityLock_Object=MibTableColumn
kmGroupSecurityLock=_KmGroupSecurityLock_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,2),_KmGroupSecurityLock_Type())
kmGroupSecurityLock.setMaxAccess(_J)
if mibBuilder.loadTexts:kmGroupSecurityLock.setStatus(_A)
_KmGroupUpdateCount_Type=Integer32
_KmGroupUpdateCount_Object=MibTableColumn
kmGroupUpdateCount=_KmGroupUpdateCount_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,3),_KmGroupUpdateCount_Type())
kmGroupUpdateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupUpdateCount.setStatus(_A)
class _KmGroupEntryCreate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_KmGroupEntryCreate_Type.__name__=_G
_KmGroupEntryCreate_Object=MibTableColumn
kmGroupEntryCreate=_KmGroupEntryCreate_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,4),_KmGroupEntryCreate_Type())
kmGroupEntryCreate.setMaxAccess(_J)
if mibBuilder.loadTexts:kmGroupEntryCreate.setStatus(_A)
class _KmGroupEntryPurge_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_KmGroupEntryPurge_Type.__name__=_G
_KmGroupEntryPurge_Object=MibTableColumn
kmGroupEntryPurge=_KmGroupEntryPurge_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,5),_KmGroupEntryPurge_Type())
kmGroupEntryPurge.setMaxAccess(_J)
if mibBuilder.loadTexts:kmGroupEntryPurge.setStatus(_A)
class _KmGroupResetAll_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_KmGroupResetAll_Type.__name__=_G
_KmGroupResetAll_Object=MibTableColumn
kmGroupResetAll=_KmGroupResetAll_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,6),_KmGroupResetAll_Type())
kmGroupResetAll.setMaxAccess(_J)
if mibBuilder.loadTexts:kmGroupResetAll.setStatus(_A)
_KmGroupEntryNumber_Type=Integer32
_KmGroupEntryNumber_Object=MibTableColumn
kmGroupEntryNumber=_KmGroupEntryNumber_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,7),_KmGroupEntryNumber_Type())
kmGroupEntryNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupEntryNumber.setStatus(_A)
class _KmGroupSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('strong',1)))
_KmGroupSecurityMode_Type.__name__=_D
_KmGroupSecurityMode_Object=MibTableColumn
kmGroupSecurityMode=_KmGroupSecurityMode_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,8),_KmGroupSecurityMode_Type())
kmGroupSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupSecurityMode.setStatus(_A)
_KmGroupDataStatus_Type=Integer32
_KmGroupDataStatus_Object=MibTableColumn
kmGroupDataStatus=_KmGroupDataStatus_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,9),_KmGroupDataStatus_Type())
kmGroupDataStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupDataStatus.setStatus(_A)
_KmGroupAccountMode_Type=Integer32
_KmGroupAccountMode_Object=MibTableColumn
kmGroupAccountMode=_KmGroupAccountMode_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,10),_KmGroupAccountMode_Type())
kmGroupAccountMode.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupAccountMode.setStatus(_A)
class _KmGroupChangeAdminCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_KmGroupChangeAdminCode_Type.__name__=_G
_KmGroupChangeAdminCode_Object=MibTableColumn
kmGroupChangeAdminCode=_KmGroupChangeAdminCode_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,11),_KmGroupChangeAdminCode_Type())
kmGroupChangeAdminCode.setMaxAccess(_J)
if mibBuilder.loadTexts:kmGroupChangeAdminCode.setStatus(_A)
_KmGroupAccountBalanceBase_Type=Integer32
_KmGroupAccountBalanceBase_Object=MibTableColumn
kmGroupAccountBalanceBase=_KmGroupAccountBalanceBase_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,12),_KmGroupAccountBalanceBase_Type())
kmGroupAccountBalanceBase.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupAccountBalanceBase.setStatus(_A)
_KmGroupAccountBalanceMax_Type=Integer32
_KmGroupAccountBalanceMax_Object=MibTableColumn
kmGroupAccountBalanceMax=_KmGroupAccountBalanceMax_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,13),_KmGroupAccountBalanceMax_Type())
kmGroupAccountBalanceMax.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupAccountBalanceMax.setStatus(_A)
_KmGroupAccountErrorReport_Type=Integer32
_KmGroupAccountErrorReport_Object=MibTableColumn
kmGroupAccountErrorReport=_KmGroupAccountErrorReport_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,14),_KmGroupAccountErrorReport_Type())
kmGroupAccountErrorReport.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupAccountErrorReport.setStatus(_A)
_KmGroupAccountErrorCancel_Type=Integer32
_KmGroupAccountErrorCancel_Object=MibTableColumn
kmGroupAccountErrorCancel=_KmGroupAccountErrorCancel_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,15),_KmGroupAccountErrorCancel_Type())
kmGroupAccountErrorCancel.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupAccountErrorCancel.setStatus(_A)
class _KmGroupAccountPrintPermission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('prohibit',0),('permit',1)))
_KmGroupAccountPrintPermission_Type.__name__=_D
_KmGroupAccountPrintPermission_Object=MibTableColumn
kmGroupAccountPrintPermission=_KmGroupAccountPrintPermission_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,16),_KmGroupAccountPrintPermission_Type())
kmGroupAccountPrintPermission.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupAccountPrintPermission.setStatus(_A)
class _KmGroupAccountBalancePattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('printCopy',1),('eachFunction',2)))
_KmGroupAccountBalancePattern_Type.__name__=_D
_KmGroupAccountBalancePattern_Object=MibTableColumn
kmGroupAccountBalancePattern=_KmGroupAccountBalancePattern_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,17),_KmGroupAccountBalancePattern_Type())
kmGroupAccountBalancePattern.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupAccountBalancePattern.setStatus(_A)
class _KmGroupAccountModeMain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_KmGroupAccountModeMain_Type.__name__=_D
_KmGroupAccountModeMain_Object=MibTableColumn
kmGroupAccountModeMain=_KmGroupAccountModeMain_Object((1,3,6,1,4,1,1347,42,1,2,1,1,1,18),_KmGroupAccountModeMain_Type())
kmGroupAccountModeMain.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupAccountModeMain.setStatus(_A)
_KmGroupTable_Object=MibTable
kmGroupTable=_KmGroupTable_Object((1,3,6,1,4,1,1347,42,1,2,1,2))
if mibBuilder.loadTexts:kmGroupTable.setStatus(_A)
_KmGroupEntry_Object=MibTableRow
kmGroupEntry=_KmGroupEntry_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1))
kmGroupEntry.setIndexNames((0,_E,_F),(0,_H,_W))
if mibBuilder.loadTexts:kmGroupEntry.setStatus(_A)
_KmGroupIndex_Type=Integer32
_KmGroupIndex_Object=MibTableColumn
kmGroupIndex=_KmGroupIndex_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,1),_KmGroupIndex_Type())
kmGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kmGroupIndex.setStatus(_A)
class _KmGroupAccountNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_KmGroupAccountNumber_Type.__name__=_G
_KmGroupAccountNumber_Object=MibTableColumn
kmGroupAccountNumber=_KmGroupAccountNumber_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,2),_KmGroupAccountNumber_Type())
kmGroupAccountNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupAccountNumber.setStatus(_A)
class _KmGroupCaption_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KmGroupCaption_Type.__name__=_G
_KmGroupCaption_Object=MibTableColumn
kmGroupCaption=_KmGroupCaption_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,3),_KmGroupCaption_Type())
kmGroupCaption.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupCaption.setStatus(_A)
_KmGroupPrinterCSetRef_Type=Integer32
_KmGroupPrinterCSetRef_Object=MibTableColumn
kmGroupPrinterCSetRef=_KmGroupPrinterCSetRef_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,4),_KmGroupPrinterCSetRef_Type())
kmGroupPrinterCSetRef.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupPrinterCSetRef.setStatus(_A)
_KmGroupCopierCSetRef_Type=Integer32
_KmGroupCopierCSetRef_Object=MibTableColumn
kmGroupCopierCSetRef=_KmGroupCopierCSetRef_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,5),_KmGroupCopierCSetRef_Type())
kmGroupCopierCSetRef.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupCopierCSetRef.setStatus(_A)
_KmGroupFAXCSetRef_Type=Integer32
_KmGroupFAXCSetRef_Object=MibTableColumn
kmGroupFAXCSetRef=_KmGroupFAXCSetRef_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,6),_KmGroupFAXCSetRef_Type())
kmGroupFAXCSetRef.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupFAXCSetRef.setStatus(_A)
_KmGroupScannerCSetRef_Type=Integer32
_KmGroupScannerCSetRef_Object=MibTableColumn
kmGroupScannerCSetRef=_KmGroupScannerCSetRef_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,7),_KmGroupScannerCSetRef_Type())
kmGroupScannerCSetRef.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupScannerCSetRef.setStatus(_A)
_KmGroupAccountBalance_Type=Integer32
_KmGroupAccountBalance_Object=MibTableColumn
kmGroupAccountBalance=_KmGroupAccountBalance_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,8),_KmGroupAccountBalance_Type())
kmGroupAccountBalance.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupAccountBalance.setStatus(_A)
class _KmGroupAccountUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(7,8)));namedValues=NamedValues(*(('impressions',7),('sheets',8)))
_KmGroupAccountUnit_Type.__name__=_D
_KmGroupAccountUnit_Object=MibTableColumn
kmGroupAccountUnit=_KmGroupAccountUnit_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,9),_KmGroupAccountUnit_Type())
kmGroupAccountUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupAccountUnit.setStatus(_A)
class _KmGroupAccountStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_KmGroupAccountStatus_Type.__name__=_D
_KmGroupAccountStatus_Object=MibTableColumn
kmGroupAccountStatus=_KmGroupAccountStatus_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,10),_KmGroupAccountStatus_Type())
kmGroupAccountStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupAccountStatus.setStatus(_A)
class _KmGroupAccountReset_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_KmGroupAccountReset_Type.__name__=_G
_KmGroupAccountReset_Object=MibTableColumn
kmGroupAccountReset=_KmGroupAccountReset_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,11),_KmGroupAccountReset_Type())
kmGroupAccountReset.setMaxAccess(_J)
if mibBuilder.loadTexts:kmGroupAccountReset.setStatus(_A)
class _KmGroupSubCaption_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KmGroupSubCaption_Type.__name__=_G
_KmGroupSubCaption_Object=MibTableColumn
kmGroupSubCaption=_KmGroupSubCaption_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,12),_KmGroupSubCaption_Type())
kmGroupSubCaption.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupSubCaption.setStatus(_A)
_KmGroupFAXReceiveCSetRef_Type=Integer32
_KmGroupFAXReceiveCSetRef_Object=MibTableColumn
kmGroupFAXReceiveCSetRef=_KmGroupFAXReceiveCSetRef_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,13),_KmGroupFAXReceiveCSetRef_Type())
kmGroupFAXReceiveCSetRef.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupFAXReceiveCSetRef.setStatus(_A)
_KmGroupMediaKindCSetRef_Type=Integer32
_KmGroupMediaKindCSetRef_Object=MibTableColumn
kmGroupMediaKindCSetRef=_KmGroupMediaKindCSetRef_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,14),_KmGroupMediaKindCSetRef_Type())
kmGroupMediaKindCSetRef.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupMediaKindCSetRef.setStatus(_A)
_KmGroupFAXSendTime_Type=Integer32
_KmGroupFAXSendTime_Object=MibTableColumn
kmGroupFAXSendTime=_KmGroupFAXSendTime_Object((1,3,6,1,4,1,1347,42,1,2,1,2,1,15),_KmGroupFAXSendTime_Type())
kmGroupFAXSendTime.setMaxAccess(_B)
if mibBuilder.loadTexts:kmGroupFAXSendTime.setStatus(_A)
_KmGroupMediaKindTable_Object=MibTable
kmGroupMediaKindTable=_KmGroupMediaKindTable_Object((1,3,6,1,4,1,1347,42,1,2,1,3))
if mibBuilder.loadTexts:kmGroupMediaKindTable.setStatus(_A)
_KmGroupMediaKindEntry_Object=MibTableRow
kmGroupMediaKindEntry=_KmGroupMediaKindEntry_Object((1,3,6,1,4,1,1347,42,1,2,1,3,1))
kmGroupMediaKindEntry.setIndexNames((0,_E,_F),(0,_H,_X))
if mibBuilder.loadTexts:kmGroupMediaKindEntry.setStatus(_A)
_KmGroupMediaKindIndex_Type=Integer32
_KmGroupMediaKindIndex_Object=MibTableColumn
kmGroupMediaKindIndex=_KmGroupMediaKindIndex_Object((1,3,6,1,4,1,1347,42,1,2,1,3,1,1),_KmGroupMediaKindIndex_Type())
kmGroupMediaKindIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kmGroupMediaKindIndex.setStatus(_A)
_KmGroupMediaSizeIndex_Type=Integer32
_KmGroupMediaSizeIndex_Object=MibTableColumn
kmGroupMediaSizeIndex=_KmGroupMediaSizeIndex_Object((1,3,6,1,4,1,1347,42,1,2,1,3,1,2),_KmGroupMediaSizeIndex_Type())
kmGroupMediaSizeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupMediaSizeIndex.setStatus(_A)
_KmGroupMediaTypeIndex_Type=Integer32
_KmGroupMediaTypeIndex_Object=MibTableColumn
kmGroupMediaTypeIndex=_KmGroupMediaTypeIndex_Object((1,3,6,1,4,1,1347,42,1,2,1,3,1,3),_KmGroupMediaTypeIndex_Type())
kmGroupMediaTypeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:kmGroupMediaTypeIndex.setStatus(_A)
_KmResource_ObjectIdentity=ObjectIdentity
kmResource=_KmResource_ObjectIdentity((1,3,6,1,4,1,1347,42,2))
_KmMedia_ObjectIdentity=ObjectIdentity
kmMedia=_KmMedia_ObjectIdentity((1,3,6,1,4,1,1347,42,2,1))
_KmMediaTable_Object=MibTable
kmMediaTable=_KmMediaTable_Object((1,3,6,1,4,1,1347,42,2,1,1))
if mibBuilder.loadTexts:kmMediaTable.setStatus(_A)
_KmMediaEntry_Object=MibTableRow
kmMediaEntry=_KmMediaEntry_Object((1,3,6,1,4,1,1347,42,2,1,1,1))
kmMediaEntry.setIndexNames((0,_E,_F),(0,_H,_Y))
if mibBuilder.loadTexts:kmMediaEntry.setStatus(_A)
_KmMediaIndex_Type=Integer32
_KmMediaIndex_Object=MibTableColumn
kmMediaIndex=_KmMediaIndex_Object((1,3,6,1,4,1,1347,42,2,1,1,1,1),_KmMediaIndex_Type())
kmMediaIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kmMediaIndex.setStatus(_A)
class _KmMediaName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KmMediaName_Type.__name__=_G
_KmMediaName_Object=MibTableColumn
kmMediaName=_KmMediaName_Object((1,3,6,1,4,1,1347,42,2,1,1,1,2),_KmMediaName_Type())
kmMediaName.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMediaName.setStatus(_A)
class _KmMediaSizeUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_Z,3),(_a,4)))
_KmMediaSizeUnit_Type.__name__=_D
_KmMediaSizeUnit_Object=MibTableColumn
kmMediaSizeUnit=_KmMediaSizeUnit_Object((1,3,6,1,4,1,1347,42,2,1,1,1,3),_KmMediaSizeUnit_Type())
kmMediaSizeUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMediaSizeUnit.setStatus(_A)
_KmMediaLongEdgeSize_Type=Integer32
_KmMediaLongEdgeSize_Object=MibTableColumn
kmMediaLongEdgeSize=_KmMediaLongEdgeSize_Object((1,3,6,1,4,1,1347,42,2,1,1,1,4),_KmMediaLongEdgeSize_Type())
kmMediaLongEdgeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMediaLongEdgeSize.setStatus(_A)
_KmMediaShortEdgeSize_Type=Integer32
_KmMediaShortEdgeSize_Object=MibTableColumn
kmMediaShortEdgeSize=_KmMediaShortEdgeSize_Object((1,3,6,1,4,1,1347,42,2,1,1,1,5),_KmMediaShortEdgeSize_Type())
kmMediaShortEdgeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMediaShortEdgeSize.setStatus(_A)
_KmMediaCounterItem_Type=Integer32
_KmMediaCounterItem_Object=MibTableColumn
kmMediaCounterItem=_KmMediaCounterItem_Object((1,3,6,1,4,1,1347,42,2,1,1,1,6),_KmMediaCounterItem_Type())
kmMediaCounterItem.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMediaCounterItem.setStatus(_A)
_KmColorMode_ObjectIdentity=ObjectIdentity
kmColorMode=_KmColorMode_ObjectIdentity((1,3,6,1,4,1,1347,42,2,2))
_KmColorModeTable_Object=MibTable
kmColorModeTable=_KmColorModeTable_Object((1,3,6,1,4,1,1347,42,2,2,1))
if mibBuilder.loadTexts:kmColorModeTable.setStatus(_A)
_KmColorModeEntry_Object=MibTableRow
kmColorModeEntry=_KmColorModeEntry_Object((1,3,6,1,4,1,1347,42,2,2,1,1))
kmColorModeEntry.setIndexNames((0,_E,_F),(0,_H,_M))
if mibBuilder.loadTexts:kmColorModeEntry.setStatus(_A)
_KmColorModeIndex_Type=Integer32
_KmColorModeIndex_Object=MibTableColumn
kmColorModeIndex=_KmColorModeIndex_Object((1,3,6,1,4,1,1347,42,2,2,1,1,1),_KmColorModeIndex_Type())
kmColorModeIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kmColorModeIndex.setStatus(_A)
class _KmColorModeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KmColorModeName_Type.__name__=_G
_KmColorModeName_Object=MibTableColumn
kmColorModeName=_KmColorModeName_Object((1,3,6,1,4,1,1347,42,2,2,1,1,2),_KmColorModeName_Type())
kmColorModeName.setMaxAccess(_B)
if mibBuilder.loadTexts:kmColorModeName.setStatus(_A)
_KmColorModeCounterItem_Type=Integer32
_KmColorModeCounterItem_Object=MibTableColumn
kmColorModeCounterItem=_KmColorModeCounterItem_Object((1,3,6,1,4,1,1347,42,2,2,1,1,3),_KmColorModeCounterItem_Type())
kmColorModeCounterItem.setMaxAccess(_B)
if mibBuilder.loadTexts:kmColorModeCounterItem.setStatus(_A)
_KmMFP_ObjectIdentity=ObjectIdentity
kmMFP=_KmMFP_ObjectIdentity((1,3,6,1,4,1,1347,42,3))
_KmMFPCounter_ObjectIdentity=ObjectIdentity
kmMFPCounter=_KmMFPCounter_ObjectIdentity((1,3,6,1,4,1,1347,42,3,1))
_KmMFPCounterTable_Object=MibTable
kmMFPCounterTable=_KmMFPCounterTable_Object((1,3,6,1,4,1,1347,42,3,1,1))
if mibBuilder.loadTexts:kmMFPCounterTable.setStatus(_A)
_KmMFPCounterEntry_Object=MibTableRow
kmMFPCounterEntry=_KmMFPCounterEntry_Object((1,3,6,1,4,1,1347,42,3,1,1,1))
kmMFPCounterEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:kmMFPCounterEntry.setStatus(_A)
_KmMFPCounterItem_Type=Integer32
_KmMFPCounterItem_Object=MibTableColumn
kmMFPCounterItem=_KmMFPCounterItem_Object((1,3,6,1,4,1,1347,42,3,1,1,1,1),_KmMFPCounterItem_Type())
kmMFPCounterItem.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPCounterItem.setStatus(_A)
_KmMFPColorModeCounterTable_Object=MibTable
kmMFPColorModeCounterTable=_KmMFPColorModeCounterTable_Object((1,3,6,1,4,1,1347,42,3,1,2))
if mibBuilder.loadTexts:kmMFPColorModeCounterTable.setStatus(_A)
_KmMFPColorModeCounterEntry_Object=MibTableRow
kmMFPColorModeCounterEntry=_KmMFPColorModeCounterEntry_Object((1,3,6,1,4,1,1347,42,3,1,2,1))
kmMFPColorModeCounterEntry.setIndexNames((0,_E,_F),(0,_H,_M))
if mibBuilder.loadTexts:kmMFPColorModeCounterEntry.setStatus(_A)
_KmMFPColorModeCounterItem_Type=Integer32
_KmMFPColorModeCounterItem_Object=MibTableColumn
kmMFPColorModeCounterItem=_KmMFPColorModeCounterItem_Object((1,3,6,1,4,1,1347,42,3,1,2,1,1),_KmMFPColorModeCounterItem_Type())
kmMFPColorModeCounterItem.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPColorModeCounterItem.setStatus(_A)
_KmMFPScanCounterTable_Object=MibTable
kmMFPScanCounterTable=_KmMFPScanCounterTable_Object((1,3,6,1,4,1,1347,42,3,1,3))
if mibBuilder.loadTexts:kmMFPScanCounterTable.setStatus(_A)
_KmMFPScanCounterEntry_Object=MibTableRow
kmMFPScanCounterEntry=_KmMFPScanCounterEntry_Object((1,3,6,1,4,1,1347,42,3,1,3,1))
kmMFPScanCounterEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:kmMFPScanCounterEntry.setStatus(_A)
_KmMFPScanCounterItem_Type=Integer32
_KmMFPScanCounterItem_Object=MibTableColumn
kmMFPScanCounterItem=_KmMFPScanCounterItem_Object((1,3,6,1,4,1,1347,42,3,1,3,1,1),_KmMFPScanCounterItem_Type())
kmMFPScanCounterItem.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPScanCounterItem.setStatus(_A)
_KmMFPDevice_ObjectIdentity=ObjectIdentity
kmMFPDevice=_KmMFPDevice_ObjectIdentity((1,3,6,1,4,1,1347,42,3,2))
_KmMFPDevicePrinter_ObjectIdentity=ObjectIdentity
kmMFPDevicePrinter=_KmMFPDevicePrinter_ObjectIdentity((1,3,6,1,4,1,1347,42,3,2,1))
_KmMFPPrinterGeneralTable_Object=MibTable
kmMFPPrinterGeneralTable=_KmMFPPrinterGeneralTable_Object((1,3,6,1,4,1,1347,42,3,2,1,1))
if mibBuilder.loadTexts:kmMFPPrinterGeneralTable.setStatus(_A)
_KmMFPPrinterGeneralEntry_Object=MibTableRow
kmMFPPrinterGeneralEntry=_KmMFPPrinterGeneralEntry_Object((1,3,6,1,4,1,1347,42,3,2,1,1,1))
kmMFPPrinterGeneralEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:kmMFPPrinterGeneralEntry.setStatus(_A)
class _KmMFPPrinterLocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,81)));namedValues=NamedValues(*(('overSea',1),('japan',81)))
_KmMFPPrinterLocalization_Type.__name__=_D
_KmMFPPrinterLocalization_Object=MibTableColumn
kmMFPPrinterLocalization=_KmMFPPrinterLocalization_Object((1,3,6,1,4,1,1347,42,3,2,1,1,1,1),_KmMFPPrinterLocalization_Type())
kmMFPPrinterLocalization.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPPrinterLocalization.setStatus(_A)
_KmMFPPrinterLocalSubCode_Type=Integer32
_KmMFPPrinterLocalSubCode_Object=MibTableColumn
kmMFPPrinterLocalSubCode=_KmMFPPrinterLocalSubCode_Object((1,3,6,1,4,1,1347,42,3,2,1,1,1,2),_KmMFPPrinterLocalSubCode_Type())
kmMFPPrinterLocalSubCode.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPPrinterLocalSubCode.setStatus(_A)
_KmMFPDeviceCopier_ObjectIdentity=ObjectIdentity
kmMFPDeviceCopier=_KmMFPDeviceCopier_ObjectIdentity((1,3,6,1,4,1,1347,42,3,2,2))
_KmMFPCopierGeneralTable_Object=MibTable
kmMFPCopierGeneralTable=_KmMFPCopierGeneralTable_Object((1,3,6,1,4,1,1347,42,3,2,2,1))
if mibBuilder.loadTexts:kmMFPCopierGeneralTable.setStatus(_A)
_KmMFPCopierGeneralEntry_Object=MibTableRow
kmMFPCopierGeneralEntry=_KmMFPCopierGeneralEntry_Object((1,3,6,1,4,1,1347,42,3,2,2,1,1))
kmMFPCopierGeneralEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:kmMFPCopierGeneralEntry.setStatus(_A)
class _KmMFPCopierLocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,31,61,81)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,31),(_Q,61),(_R,81)))
_KmMFPCopierLocalization_Type.__name__=_D
_KmMFPCopierLocalization_Object=MibTableColumn
kmMFPCopierLocalization=_KmMFPCopierLocalization_Object((1,3,6,1,4,1,1347,42,3,2,2,1,1,1),_KmMFPCopierLocalization_Type())
kmMFPCopierLocalization.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPCopierLocalization.setStatus(_A)
_KmMFPCopierLocalSubCode_Type=Integer32
_KmMFPCopierLocalSubCode_Object=MibTableColumn
kmMFPCopierLocalSubCode=_KmMFPCopierLocalSubCode_Object((1,3,6,1,4,1,1347,42,3,2,2,1,1,2),_KmMFPCopierLocalSubCode_Type())
kmMFPCopierLocalSubCode.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPCopierLocalSubCode.setStatus(_A)
_KmMFPDeviceScanner_ObjectIdentity=ObjectIdentity
kmMFPDeviceScanner=_KmMFPDeviceScanner_ObjectIdentity((1,3,6,1,4,1,1347,42,3,2,3))
_KmMFPScannerGeneralTable_Object=MibTable
kmMFPScannerGeneralTable=_KmMFPScannerGeneralTable_Object((1,3,6,1,4,1,1347,42,3,2,3,1))
if mibBuilder.loadTexts:kmMFPScannerGeneralTable.setStatus(_A)
_KmMFPScannerGeneralEntry_Object=MibTableRow
kmMFPScannerGeneralEntry=_KmMFPScannerGeneralEntry_Object((1,3,6,1,4,1,1347,42,3,2,3,1,1))
kmMFPScannerGeneralEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:kmMFPScannerGeneralEntry.setStatus(_A)
class _KmMFPScannerLocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,31,61,81)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,31),(_Q,61),(_R,81)))
_KmMFPScannerLocalization_Type.__name__=_D
_KmMFPScannerLocalization_Object=MibTableColumn
kmMFPScannerLocalization=_KmMFPScannerLocalization_Object((1,3,6,1,4,1,1347,42,3,2,3,1,1,1),_KmMFPScannerLocalization_Type())
kmMFPScannerLocalization.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPScannerLocalization.setStatus(_A)
_KmMFPScannerLocalSubCode_Type=Integer32
_KmMFPScannerLocalSubCode_Object=MibTableColumn
kmMFPScannerLocalSubCode=_KmMFPScannerLocalSubCode_Object((1,3,6,1,4,1,1347,42,3,2,3,1,1,2),_KmMFPScannerLocalSubCode_Type())
kmMFPScannerLocalSubCode.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPScannerLocalSubCode.setStatus(_A)
class _KmMFPScannerAccountMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('imageScan',1),('networkScan',2)))
_KmMFPScannerAccountMode_Type.__name__=_D
_KmMFPScannerAccountMode_Object=MibTableColumn
kmMFPScannerAccountMode=_KmMFPScannerAccountMode_Object((1,3,6,1,4,1,1347,42,3,2,3,1,1,3),_KmMFPScannerAccountMode_Type())
kmMFPScannerAccountMode.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPScannerAccountMode.setStatus(_A)
_KmMFPScannerDocProcessorTable_Object=MibTable
kmMFPScannerDocProcessorTable=_KmMFPScannerDocProcessorTable_Object((1,3,6,1,4,1,1347,42,3,2,3,2))
if mibBuilder.loadTexts:kmMFPScannerDocProcessorTable.setStatus(_A)
_KmMFPScannerDocProcessorEntry_Object=MibTableRow
kmMFPScannerDocProcessorEntry=_KmMFPScannerDocProcessorEntry_Object((1,3,6,1,4,1,1347,42,3,2,3,2,1))
kmMFPScannerDocProcessorEntry.setIndexNames((0,_E,_F),(0,_H,_b))
if mibBuilder.loadTexts:kmMFPScannerDocProcessorEntry.setStatus(_A)
_KmMFPDocProcessorIndex_Type=Integer32
_KmMFPDocProcessorIndex_Object=MibTableColumn
kmMFPDocProcessorIndex=_KmMFPDocProcessorIndex_Object((1,3,6,1,4,1,1347,42,3,2,3,2,1,1),_KmMFPDocProcessorIndex_Type())
kmMFPDocProcessorIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kmMFPDocProcessorIndex.setStatus(_A)
class _KmMFPDocProcessorModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KmMFPDocProcessorModel_Type.__name__=_G
_KmMFPDocProcessorModel_Object=MibTableColumn
kmMFPDocProcessorModel=_KmMFPDocProcessorModel_Object((1,3,6,1,4,1,1347,42,3,2,3,2,1,2),_KmMFPDocProcessorModel_Type())
kmMFPDocProcessorModel.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPDocProcessorModel.setStatus(_A)
class _KmMFPDocProcessorAbsolteModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KmMFPDocProcessorAbsolteModel_Type.__name__=_G
_KmMFPDocProcessorAbsolteModel_Object=MibTableColumn
kmMFPDocProcessorAbsolteModel=_KmMFPDocProcessorAbsolteModel_Object((1,3,6,1,4,1,1347,42,3,2,3,2,1,3),_KmMFPDocProcessorAbsolteModel_Type())
kmMFPDocProcessorAbsolteModel.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPDocProcessorAbsolteModel.setStatus(_A)
_KmMFPDeviceFAX_ObjectIdentity=ObjectIdentity
kmMFPDeviceFAX=_KmMFPDeviceFAX_ObjectIdentity((1,3,6,1,4,1,1347,42,3,2,4))
_KmMFPFAXGeneralTable_Object=MibTable
kmMFPFAXGeneralTable=_KmMFPFAXGeneralTable_Object((1,3,6,1,4,1,1347,42,3,2,4,1))
if mibBuilder.loadTexts:kmMFPFAXGeneralTable.setStatus(_A)
_KmMFPFAXGeneralEntry_Object=MibTableRow
kmMFPFAXGeneralEntry=_KmMFPFAXGeneralEntry_Object((1,3,6,1,4,1,1347,42,3,2,4,1,1))
kmMFPFAXGeneralEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:kmMFPFAXGeneralEntry.setStatus(_A)
class _KmMFPFAXLocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,31,61,81)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,31),(_Q,61),(_R,81)))
_KmMFPFAXLocalization_Type.__name__=_D
_KmMFPFAXLocalization_Object=MibTableColumn
kmMFPFAXLocalization=_KmMFPFAXLocalization_Object((1,3,6,1,4,1,1347,42,3,2,4,1,1,1),_KmMFPFAXLocalization_Type())
kmMFPFAXLocalization.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPFAXLocalization.setStatus(_A)
_KmMFPFAXLocalSubCode_Type=Integer32
_KmMFPFAXLocalSubCode_Object=MibTableColumn
kmMFPFAXLocalSubCode=_KmMFPFAXLocalSubCode_Object((1,3,6,1,4,1,1347,42,3,2,4,1,1,2),_KmMFPFAXLocalSubCode_Type())
kmMFPFAXLocalSubCode.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPFAXLocalSubCode.setStatus(_A)
_KmMFPDeviceGeneral_ObjectIdentity=ObjectIdentity
kmMFPDeviceGeneral=_KmMFPDeviceGeneral_ObjectIdentity((1,3,6,1,4,1,1347,42,3,2,5))
_KmMFPGeneralTable_Object=MibTable
kmMFPGeneralTable=_KmMFPGeneralTable_Object((1,3,6,1,4,1,1347,42,3,2,5,1))
if mibBuilder.loadTexts:kmMFPGeneralTable.setStatus(_A)
_KmMFPGeneralEntry_Object=MibTableRow
kmMFPGeneralEntry=_KmMFPGeneralEntry_Object((1,3,6,1,4,1,1347,42,3,2,5,1,1))
kmMFPGeneralEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:kmMFPGeneralEntry.setStatus(_A)
_KmMFPFunctionControl_Type=Integer32
_KmMFPFunctionControl_Object=MibTableColumn
kmMFPFunctionControl=_KmMFPFunctionControl_Object((1,3,6,1,4,1,1347,42,3,2,5,1,1,1),_KmMFPFunctionControl_Type())
kmMFPFunctionControl.setMaxAccess(_C)
if mibBuilder.loadTexts:kmMFPFunctionControl.setStatus(_K)
class _KmMFPDeviceDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_KmMFPDeviceDateTime_Type.__name__=_G
_KmMFPDeviceDateTime_Object=MibTableColumn
kmMFPDeviceDateTime=_KmMFPDeviceDateTime_Object((1,3,6,1,4,1,1347,42,3,2,5,1,1,2),_KmMFPDeviceDateTime_Type())
kmMFPDeviceDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:kmMFPDeviceDateTime.setStatus(_K)
_KmGeneral_ObjectIdentity=ObjectIdentity
kmGeneral=_KmGeneral_ObjectIdentity((1,3,6,1,4,1,1347,42,5))
_KmGeneralTable_Object=MibTable
kmGeneralTable=_KmGeneralTable_Object((1,3,6,1,4,1,1347,42,5,1))
if mibBuilder.loadTexts:kmGeneralTable.setStatus(_A)
_KmGeneralEntry_Object=MibTableRow
kmGeneralEntry=_KmGeneralEntry_Object((1,3,6,1,4,1,1347,42,5,1,1))
kmGeneralEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:kmGeneralEntry.setStatus(_A)
class _KmProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KmProductName_Type.__name__=_G
_KmProductName_Object=MibTableColumn
kmProductName=_KmProductName_Object((1,3,6,1,4,1,1347,42,5,1,1,1),_KmProductName_Type())
kmProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:kmProductName.setStatus(_A)
class _KmAbsoluteName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KmAbsoluteName_Type.__name__=_G
_KmAbsoluteName_Object=MibTableColumn
kmAbsoluteName=_KmAbsoluteName_Object((1,3,6,1,4,1,1347,42,5,1,1,2),_KmAbsoluteName_Type())
kmAbsoluteName.setMaxAccess(_B)
if mibBuilder.loadTexts:kmAbsoluteName.setStatus(_A)
class _KmDefaultAgent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('status',1),('copy',2),('send',3),('docbox',4)))
_KmDefaultAgent_Type.__name__=_D
_KmDefaultAgent_Object=MibTableColumn
kmDefaultAgent=_KmDefaultAgent_Object((1,3,6,1,4,1,1347,42,5,1,1,3),_KmDefaultAgent_Type())
kmDefaultAgent.setMaxAccess(_C)
if mibBuilder.loadTexts:kmDefaultAgent.setStatus(_A)
_KmAgentResumeMode_Type=PresentOnOff
_KmAgentResumeMode_Object=MibTableColumn
kmAgentResumeMode=_KmAgentResumeMode_Object((1,3,6,1,4,1,1347,42,5,1,1,4),_KmAgentResumeMode_Type())
kmAgentResumeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:kmAgentResumeMode.setStatus(_A)
class _KmAgentResumeTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_KmAgentResumeTimeout_Type.__name__=_D
_KmAgentResumeTimeout_Object=MibTableColumn
kmAgentResumeTimeout=_KmAgentResumeTimeout_Object((1,3,6,1,4,1,1347,42,5,1,1,5),_KmAgentResumeTimeout_Type())
kmAgentResumeTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:kmAgentResumeTimeout.setStatus(_A)
_KmOneTouchKeyNum_Type=Integer32
_KmOneTouchKeyNum_Object=MibTableColumn
kmOneTouchKeyNum=_KmOneTouchKeyNum_Object((1,3,6,1,4,1,1347,42,5,1,1,8),_KmOneTouchKeyNum_Type())
kmOneTouchKeyNum.setMaxAccess(_B)
if mibBuilder.loadTexts:kmOneTouchKeyNum.setStatus(_A)
_KmOneTouchShiftNum_Type=Integer32
_KmOneTouchShiftNum_Object=MibTableColumn
kmOneTouchShiftNum=_KmOneTouchShiftNum_Object((1,3,6,1,4,1,1347,42,5,1,1,9),_KmOneTouchShiftNum_Type())
kmOneTouchShiftNum.setMaxAccess(_B)
if mibBuilder.loadTexts:kmOneTouchShiftNum.setStatus(_A)
class _KmLocalTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(36,36));fixedLength=36
_KmLocalTime_Type.__name__=_L
_KmLocalTime_Object=MibTableColumn
kmLocalTime=_KmLocalTime_Object((1,3,6,1,4,1,1347,42,5,1,1,10),_KmLocalTime_Type())
kmLocalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:kmLocalTime.setStatus(_A)
class _KmTimeFormat_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_KmTimeFormat_Type.__name__=_L
_KmTimeFormat_Object=MibTableColumn
kmTimeFormat=_KmTimeFormat_Object((1,3,6,1,4,1,1347,42,5,1,1,11),_KmTimeFormat_Type())
kmTimeFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:kmTimeFormat.setStatus(_A)
_KmTimeZone_Type=Integer32
_KmTimeZone_Object=MibTableColumn
kmTimeZone=_KmTimeZone_Object((1,3,6,1,4,1,1347,42,5,1,1,12),_KmTimeZone_Type())
kmTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:kmTimeZone.setStatus(_A)
class _KmPanelSizeUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_Z,3),(_a,4)))
_KmPanelSizeUnit_Type.__name__=_D
_KmPanelSizeUnit_Object=MibTableColumn
kmPanelSizeUnit=_KmPanelSizeUnit_Object((1,3,6,1,4,1,1347,42,5,1,1,13),_KmPanelSizeUnit_Type())
kmPanelSizeUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:kmPanelSizeUnit.setStatus(_A)
_KmPrescribeEscape_Type=Integer32
_KmPrescribeEscape_Object=MibTableColumn
kmPrescribeEscape=_KmPrescribeEscape_Object((1,3,6,1,4,1,1347,42,5,1,1,14),_KmPrescribeEscape_Type())
kmPrescribeEscape.setMaxAccess(_C)
if mibBuilder.loadTexts:kmPrescribeEscape.setStatus(_A)
class _KmConsoleDisableEx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*(('partialLock',1),('enabled',3),('disabled',4)))
_KmConsoleDisableEx_Type.__name__=_D
_KmConsoleDisableEx_Object=MibTableColumn
kmConsoleDisableEx=_KmConsoleDisableEx_Object((1,3,6,1,4,1,1347,42,5,1,1,15),_KmConsoleDisableEx_Type())
kmConsoleDisableEx.setMaxAccess(_C)
if mibBuilder.loadTexts:kmConsoleDisableEx.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'kyocera':kyocera,'kmCommon':kmCommon,'kmAccounting':kmAccounting,'kmCounterSet':kmCounterSet,'kmCounterSetTable':kmCounterSetTable,'kmCounterSetEntry':kmCounterSetEntry,_S:kmCounterSetIndex,_T:kmCounterSetItemIndex,'kmCounterItem':kmCounterItem,'kmCounterMediaRef':kmCounterMediaRef,'kmCounterColorModeRef':kmCounterColorModeRef,'kmAccountBalanceItem':kmAccountBalanceItem,'kmAccountBalanceStatus':kmAccountBalanceStatus,'kmAccountRestriction':kmAccountRestriction,'kmGroup':kmGroup,'kmGroupLevel1':kmGroupLevel1,'kmGroupConfigTable':kmGroupConfigTable,'kmGroupConfigEntry':kmGroupConfigEntry,'kmGroupCodeWidth':kmGroupCodeWidth,'kmGroupSecurityLock':kmGroupSecurityLock,'kmGroupUpdateCount':kmGroupUpdateCount,'kmGroupEntryCreate':kmGroupEntryCreate,'kmGroupEntryPurge':kmGroupEntryPurge,'kmGroupResetAll':kmGroupResetAll,'kmGroupEntryNumber':kmGroupEntryNumber,'kmGroupSecurityMode':kmGroupSecurityMode,'kmGroupDataStatus':kmGroupDataStatus,'kmGroupAccountMode':kmGroupAccountMode,'kmGroupChangeAdminCode':kmGroupChangeAdminCode,'kmGroupAccountBalanceBase':kmGroupAccountBalanceBase,'kmGroupAccountBalanceMax':kmGroupAccountBalanceMax,'kmGroupAccountErrorReport':kmGroupAccountErrorReport,'kmGroupAccountErrorCancel':kmGroupAccountErrorCancel,'kmGroupAccountPrintPermission':kmGroupAccountPrintPermission,'kmGroupAccountBalancePattern':kmGroupAccountBalancePattern,'kmGroupAccountModeMain':kmGroupAccountModeMain,'kmGroupTable':kmGroupTable,'kmGroupEntry':kmGroupEntry,_W:kmGroupIndex,'kmGroupAccountNumber':kmGroupAccountNumber,'kmGroupCaption':kmGroupCaption,'kmGroupPrinterCSetRef':kmGroupPrinterCSetRef,'kmGroupCopierCSetRef':kmGroupCopierCSetRef,'kmGroupFAXCSetRef':kmGroupFAXCSetRef,'kmGroupScannerCSetRef':kmGroupScannerCSetRef,'kmGroupAccountBalance':kmGroupAccountBalance,'kmGroupAccountUnit':kmGroupAccountUnit,'kmGroupAccountStatus':kmGroupAccountStatus,'kmGroupAccountReset':kmGroupAccountReset,'kmGroupSubCaption':kmGroupSubCaption,'kmGroupFAXReceiveCSetRef':kmGroupFAXReceiveCSetRef,'kmGroupMediaKindCSetRef':kmGroupMediaKindCSetRef,'kmGroupFAXSendTime':kmGroupFAXSendTime,'kmGroupMediaKindTable':kmGroupMediaKindTable,'kmGroupMediaKindEntry':kmGroupMediaKindEntry,_X:kmGroupMediaKindIndex,'kmGroupMediaSizeIndex':kmGroupMediaSizeIndex,'kmGroupMediaTypeIndex':kmGroupMediaTypeIndex,'kmResource':kmResource,'kmMedia':kmMedia,'kmMediaTable':kmMediaTable,'kmMediaEntry':kmMediaEntry,_Y:kmMediaIndex,'kmMediaName':kmMediaName,'kmMediaSizeUnit':kmMediaSizeUnit,'kmMediaLongEdgeSize':kmMediaLongEdgeSize,'kmMediaShortEdgeSize':kmMediaShortEdgeSize,'kmMediaCounterItem':kmMediaCounterItem,'kmColorMode':kmColorMode,'kmColorModeTable':kmColorModeTable,'kmColorModeEntry':kmColorModeEntry,_M:kmColorModeIndex,'kmColorModeName':kmColorModeName,'kmColorModeCounterItem':kmColorModeCounterItem,'kmMFP':kmMFP,'kmMFPCounter':kmMFPCounter,'kmMFPCounterTable':kmMFPCounterTable,'kmMFPCounterEntry':kmMFPCounterEntry,'kmMFPCounterItem':kmMFPCounterItem,'kmMFPColorModeCounterTable':kmMFPColorModeCounterTable,'kmMFPColorModeCounterEntry':kmMFPColorModeCounterEntry,'kmMFPColorModeCounterItem':kmMFPColorModeCounterItem,'kmMFPScanCounterTable':kmMFPScanCounterTable,'kmMFPScanCounterEntry':kmMFPScanCounterEntry,'kmMFPScanCounterItem':kmMFPScanCounterItem,'kmMFPDevice':kmMFPDevice,'kmMFPDevicePrinter':kmMFPDevicePrinter,'kmMFPPrinterGeneralTable':kmMFPPrinterGeneralTable,'kmMFPPrinterGeneralEntry':kmMFPPrinterGeneralEntry,'kmMFPPrinterLocalization':kmMFPPrinterLocalization,'kmMFPPrinterLocalSubCode':kmMFPPrinterLocalSubCode,'kmMFPDeviceCopier':kmMFPDeviceCopier,'kmMFPCopierGeneralTable':kmMFPCopierGeneralTable,'kmMFPCopierGeneralEntry':kmMFPCopierGeneralEntry,'kmMFPCopierLocalization':kmMFPCopierLocalization,'kmMFPCopierLocalSubCode':kmMFPCopierLocalSubCode,'kmMFPDeviceScanner':kmMFPDeviceScanner,'kmMFPScannerGeneralTable':kmMFPScannerGeneralTable,'kmMFPScannerGeneralEntry':kmMFPScannerGeneralEntry,'kmMFPScannerLocalization':kmMFPScannerLocalization,'kmMFPScannerLocalSubCode':kmMFPScannerLocalSubCode,'kmMFPScannerAccountMode':kmMFPScannerAccountMode,'kmMFPScannerDocProcessorTable':kmMFPScannerDocProcessorTable,'kmMFPScannerDocProcessorEntry':kmMFPScannerDocProcessorEntry,_b:kmMFPDocProcessorIndex,'kmMFPDocProcessorModel':kmMFPDocProcessorModel,'kmMFPDocProcessorAbsolteModel':kmMFPDocProcessorAbsolteModel,'kmMFPDeviceFAX':kmMFPDeviceFAX,'kmMFPFAXGeneralTable':kmMFPFAXGeneralTable,'kmMFPFAXGeneralEntry':kmMFPFAXGeneralEntry,'kmMFPFAXLocalization':kmMFPFAXLocalization,'kmMFPFAXLocalSubCode':kmMFPFAXLocalSubCode,'kmMFPDeviceGeneral':kmMFPDeviceGeneral,'kmMFPGeneralTable':kmMFPGeneralTable,'kmMFPGeneralEntry':kmMFPGeneralEntry,'kmMFPFunctionControl':kmMFPFunctionControl,'kmMFPDeviceDateTime':kmMFPDeviceDateTime,'kmGeneral':kmGeneral,'kmGeneralTable':kmGeneralTable,'kmGeneralEntry':kmGeneralEntry,'kmProductName':kmProductName,'kmAbsoluteName':kmAbsoluteName,'kmDefaultAgent':kmDefaultAgent,'kmAgentResumeMode':kmAgentResumeMode,'kmAgentResumeTimeout':kmAgentResumeTimeout,'kmOneTouchKeyNum':kmOneTouchKeyNum,'kmOneTouchShiftNum':kmOneTouchShiftNum,'kmLocalTime':kmLocalTime,'kmTimeFormat':kmTimeFormat,'kmTimeZone':kmTimeZone,'kmPanelSizeUnit':kmPanelSizeUnit,'kmPrescribeEscape':kmPrescribeEscape,'kmConsoleDisableEx':kmConsoleDisableEx})