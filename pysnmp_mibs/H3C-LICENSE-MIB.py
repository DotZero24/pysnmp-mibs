_X='h3cLicenseBindValidityPeriodRemaining'
_W='h3cLicenseOpFailedReason'
_V='h3cLicenseOpState'
_U='h3cLicenseOpString'
_T='h3cLicenseOpType'
_S='h3cLicenseOpPhysicalIndex'
_R='h3cLicenseIndex'
_Q='read-write'
_P='Unsigned32'
_O='OctetString'
_N='h3cLicenseFeatureState'
_M='h3cLicenseActivationFile'
_L='h3cLicenseOpIndex'
_K='invalid'
_J='TruthValue'
_I='h3cLicenseFeatureName'
_H='accessible-for-notify'
_G='read-create'
_F='h3cLicensePhysicalIndex'
_E='Integer32'
_D='SnmpAdminString'
_C='H3C-LICENSE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,PhysicalIndexOrZero=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex','PhysicalIndexOrZero')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
h3cLicense=ModuleIdentity((1,3,6,1,4,1,2011,10,2,145))
if mibBuilder.loadTexts:h3cLicense.setRevisions(('2013-09-18 10:00',))
_H3cLicenseScalarObjects_ObjectIdentity=ObjectIdentity
h3cLicenseScalarObjects=_H3cLicenseScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,145,1))
class _H3cLicenseNotifyEnable_Type(TruthValue):defaultValue=1
_H3cLicenseNotifyEnable_Type.__name__=_J
_H3cLicenseNotifyEnable_Object=MibScalar
h3cLicenseNotifyEnable=_H3cLicenseNotifyEnable_Object((1,3,6,1,4,1,2011,10,2,145,1,1),_H3cLicenseNotifyEnable_Type())
h3cLicenseNotifyEnable.setMaxAccess(_Q)
if mibBuilder.loadTexts:h3cLicenseNotifyEnable.setStatus(_A)
class _H3cLicenseOpEntryMaxNum_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_H3cLicenseOpEntryMaxNum_Type.__name__=_P
_H3cLicenseOpEntryMaxNum_Object=MibScalar
h3cLicenseOpEntryMaxNum=_H3cLicenseOpEntryMaxNum_Object((1,3,6,1,4,1,2011,10,2,145,1,2),_H3cLicenseOpEntryMaxNum_Type())
h3cLicenseOpEntryMaxNum.setMaxAccess(_Q)
if mibBuilder.loadTexts:h3cLicenseOpEntryMaxNum.setStatus(_A)
_H3cLicenseNextFreeOpIndex_Type=Unsigned32
_H3cLicenseNextFreeOpIndex_Object=MibScalar
h3cLicenseNextFreeOpIndex=_H3cLicenseNextFreeOpIndex_Object((1,3,6,1,4,1,2011,10,2,145,1,3),_H3cLicenseNextFreeOpIndex_Type())
h3cLicenseNextFreeOpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseNextFreeOpIndex.setStatus(_A)
_H3cLicenseTables_ObjectIdentity=ObjectIdentity
h3cLicenseTables=_H3cLicenseTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,145,2))
_H3cLicenseDevInfoTable_Object=MibTable
h3cLicenseDevInfoTable=_H3cLicenseDevInfoTable_Object((1,3,6,1,4,1,2011,10,2,145,2,1))
if mibBuilder.loadTexts:h3cLicenseDevInfoTable.setStatus(_A)
_H3cLicenseDevInfoEntry_Object=MibTableRow
h3cLicenseDevInfoEntry=_H3cLicenseDevInfoEntry_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1))
h3cLicenseDevInfoEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cLicenseDevInfoEntry.setStatus(_A)
_H3cLicensePhysicalIndex_Type=PhysicalIndex
_H3cLicensePhysicalIndex_Object=MibTableColumn
h3cLicensePhysicalIndex=_H3cLicensePhysicalIndex_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,1),_H3cLicensePhysicalIndex_Type())
h3cLicensePhysicalIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLicensePhysicalIndex.setStatus(_A)
class _H3cLicenseSN_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseSN_Type.__name__=_D
_H3cLicenseSN_Object=MibTableColumn
h3cLicenseSN=_H3cLicenseSN_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,2),_H3cLicenseSN_Type())
h3cLicenseSN.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseSN.setStatus(_A)
class _H3cLicenseDeviceIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('keyString',2),('file',3)))
_H3cLicenseDeviceIDType_Type.__name__=_E
_H3cLicenseDeviceIDType_Object=MibTableColumn
h3cLicenseDeviceIDType=_H3cLicenseDeviceIDType_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,3),_H3cLicenseDeviceIDType_Type())
h3cLicenseDeviceIDType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseDeviceIDType.setStatus(_A)
class _H3cLicenseDeviceID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseDeviceID_Type.__name__=_D
_H3cLicenseDeviceID_Object=MibTableColumn
h3cLicenseDeviceID=_H3cLicenseDeviceID_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,4),_H3cLicenseDeviceID_Type())
h3cLicenseDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseDeviceID.setStatus(_A)
class _H3cLicenseHardwareInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseHardwareInfo_Type.__name__=_D
_H3cLicenseHardwareInfo_Object=MibTableColumn
h3cLicenseHardwareInfo=_H3cLicenseHardwareInfo_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,5),_H3cLicenseHardwareInfo_Type())
h3cLicenseHardwareInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseHardwareInfo.setStatus(_A)
_H3cLicenseMaxNum_Type=Unsigned32
_H3cLicenseMaxNum_Object=MibTableColumn
h3cLicenseMaxNum=_H3cLicenseMaxNum_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,6),_H3cLicenseMaxNum_Type())
h3cLicenseMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseMaxNum.setStatus(_A)
_H3cLicenseUsedNum_Type=Unsigned32
_H3cLicenseUsedNum_Object=MibTableColumn
h3cLicenseUsedNum=_H3cLicenseUsedNum_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,7),_H3cLicenseUsedNum_Type())
h3cLicenseUsedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseUsedNum.setStatus(_A)
_H3cLicenseRecyclableNum_Type=Unsigned32
_H3cLicenseRecyclableNum_Object=MibTableColumn
h3cLicenseRecyclableNum=_H3cLicenseRecyclableNum_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,8),_H3cLicenseRecyclableNum_Type())
h3cLicenseRecyclableNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseRecyclableNum.setStatus(_A)
class _H3cLicenseInstallType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('installInChassis',2),('installInSlot',3),('installInCPU',4)))
_H3cLicenseInstallType_Type.__name__=_E
_H3cLicenseInstallType_Object=MibTableColumn
h3cLicenseInstallType=_H3cLicenseInstallType_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,9),_H3cLicenseInstallType_Type())
h3cLicenseInstallType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseInstallType.setStatus(_A)
class _H3cLicenseFileStoragePath_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseFileStoragePath_Type.__name__=_D
_H3cLicenseFileStoragePath_Object=MibTableColumn
h3cLicenseFileStoragePath=_H3cLicenseFileStoragePath_Object((1,3,6,1,4,1,2011,10,2,145,2,1,1,10),_H3cLicenseFileStoragePath_Type())
h3cLicenseFileStoragePath.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseFileStoragePath.setStatus(_A)
_H3cLicenseGeneralTable_Object=MibTable
h3cLicenseGeneralTable=_H3cLicenseGeneralTable_Object((1,3,6,1,4,1,2011,10,2,145,2,2))
if mibBuilder.loadTexts:h3cLicenseGeneralTable.setStatus(_A)
_H3cLicenseGeneralEntry_Object=MibTableRow
h3cLicenseGeneralEntry=_H3cLicenseGeneralEntry_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1))
h3cLicenseGeneralEntry.setIndexNames((0,_C,_F),(0,_C,_R))
if mibBuilder.loadTexts:h3cLicenseGeneralEntry.setStatus(_A)
_H3cLicenseIndex_Type=Unsigned32
_H3cLicenseIndex_Object=MibTableColumn
h3cLicenseIndex=_H3cLicenseIndex_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,1),_H3cLicenseIndex_Type())
h3cLicenseIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLicenseIndex.setStatus(_A)
class _H3cLicenseFeature_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_H3cLicenseFeature_Type.__name__=_D
_H3cLicenseFeature_Object=MibTableColumn
h3cLicenseFeature=_H3cLicenseFeature_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,2),_H3cLicenseFeature_Type())
h3cLicenseFeature.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseFeature.setStatus(_A)
class _H3cLicenseProductDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_H3cLicenseProductDescr_Type.__name__=_O
_H3cLicenseProductDescr_Object=MibTableColumn
h3cLicenseProductDescr=_H3cLicenseProductDescr_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,3),_H3cLicenseProductDescr_Type())
h3cLicenseProductDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseProductDescr.setStatus(_A)
class _H3cLicenseFileDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_H3cLicenseFileDescr_Type.__name__=_D
_H3cLicenseFileDescr_Object=MibTableColumn
h3cLicenseFileDescr=_H3cLicenseFileDescr_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,4),_H3cLicenseFileDescr_Type())
h3cLicenseFileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseFileDescr.setStatus(_A)
class _H3cLicenseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),('inuse',2),('usable',3),('expired',4),('uninstalled',5),('unusable',6)))
_H3cLicenseState_Type.__name__=_E
_H3cLicenseState_Object=MibTableColumn
h3cLicenseState=_H3cLicenseState_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,5),_H3cLicenseState_Type())
h3cLicenseState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseState.setStatus(_A)
class _H3cLicenseActivationFile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseActivationFile_Type.__name__=_D
_H3cLicenseActivationFile_Object=MibTableColumn
h3cLicenseActivationFile=_H3cLicenseActivationFile_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,6),_H3cLicenseActivationFile_Type())
h3cLicenseActivationFile.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseActivationFile.setStatus(_A)
class _H3cLicenseActivationKey_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseActivationKey_Type.__name__=_D
_H3cLicenseActivationKey_Object=MibTableColumn
h3cLicenseActivationKey=_H3cLicenseActivationKey_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,7),_H3cLicenseActivationKey_Type())
h3cLicenseActivationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseActivationKey.setStatus(_A)
class _H3cLicenseLicenseKey_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseLicenseKey_Type.__name__=_D
_H3cLicenseLicenseKey_Object=MibTableColumn
h3cLicenseLicenseKey=_H3cLicenseLicenseKey_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,8),_H3cLicenseLicenseKey_Type())
h3cLicenseLicenseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseLicenseKey.setStatus(_A)
class _H3cLicenseUninstActivationFile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseUninstActivationFile_Type.__name__=_D
_H3cLicenseUninstActivationFile_Object=MibTableColumn
h3cLicenseUninstActivationFile=_H3cLicenseUninstActivationFile_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,9),_H3cLicenseUninstActivationFile_Type())
h3cLicenseUninstActivationFile.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseUninstActivationFile.setStatus(_A)
class _H3cLicenseUninstActivationKey_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseUninstActivationKey_Type.__name__=_D
_H3cLicenseUninstActivationKey_Object=MibTableColumn
h3cLicenseUninstActivationKey=_H3cLicenseUninstActivationKey_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,10),_H3cLicenseUninstActivationKey_Type())
h3cLicenseUninstActivationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseUninstActivationKey.setStatus(_A)
class _H3cLicenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('permanent',2),('daysRestricted',3),('trialDaysRestricted',4),('dateRestricted',5),('trialDateRestricted',6),('countRestricted',7),('trialCountRestricted',8)))
_H3cLicenseType_Type.__name__=_E
_H3cLicenseType_Object=MibTableColumn
h3cLicenseType=_H3cLicenseType_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,11),_H3cLicenseType_Type())
h3cLicenseType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseType.setStatus(_A)
_H3cLicenseInstalledTime_Type=DateAndTime
_H3cLicenseInstalledTime_Object=MibTableColumn
h3cLicenseInstalledTime=_H3cLicenseInstalledTime_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,12),_H3cLicenseInstalledTime_Type())
h3cLicenseInstalledTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseInstalledTime.setStatus(_A)
_H3cLicenseUninstalledTime_Type=DateAndTime
_H3cLicenseUninstalledTime_Object=MibTableColumn
h3cLicenseUninstalledTime=_H3cLicenseUninstalledTime_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,13),_H3cLicenseUninstalledTime_Type())
h3cLicenseUninstalledTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseUninstalledTime.setStatus(_A)
_H3cLicenseDaysLeft_Type=Unsigned32
_H3cLicenseDaysLeft_Object=MibTableColumn
h3cLicenseDaysLeft=_H3cLicenseDaysLeft_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,14),_H3cLicenseDaysLeft_Type())
h3cLicenseDaysLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseDaysLeft.setStatus(_A)
_H3cLicenseValidityStart_Type=DateAndTime
_H3cLicenseValidityStart_Object=MibTableColumn
h3cLicenseValidityStart=_H3cLicenseValidityStart_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,15),_H3cLicenseValidityStart_Type())
h3cLicenseValidityStart.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseValidityStart.setStatus(_A)
_H3cLicenseValidityEnd_Type=DateAndTime
_H3cLicenseValidityEnd_Object=MibTableColumn
h3cLicenseValidityEnd=_H3cLicenseValidityEnd_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,16),_H3cLicenseValidityEnd_Type())
h3cLicenseValidityEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseValidityEnd.setStatus(_A)
_H3cLicenseExpiredDays_Type=Unsigned32
_H3cLicenseExpiredDays_Object=MibTableColumn
h3cLicenseExpiredDays=_H3cLicenseExpiredDays_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,17),_H3cLicenseExpiredDays_Type())
h3cLicenseExpiredDays.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseExpiredDays.setStatus(_A)
_H3cLicenseCount_Type=Unsigned32
_H3cLicenseCount_Object=MibTableColumn
h3cLicenseCount=_H3cLicenseCount_Object((1,3,6,1,4,1,2011,10,2,145,2,2,1,18),_H3cLicenseCount_Type())
h3cLicenseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseCount.setStatus(_A)
_H3cLicenseFeatureTable_Object=MibTable
h3cLicenseFeatureTable=_H3cLicenseFeatureTable_Object((1,3,6,1,4,1,2011,10,2,145,2,3))
if mibBuilder.loadTexts:h3cLicenseFeatureTable.setStatus(_A)
_H3cLicenseFeatureEntry_Object=MibTableRow
h3cLicenseFeatureEntry=_H3cLicenseFeatureEntry_Object((1,3,6,1,4,1,2011,10,2,145,2,3,1))
h3cLicenseFeatureEntry.setIndexNames((0,_C,_F),(1,_C,_I))
if mibBuilder.loadTexts:h3cLicenseFeatureEntry.setStatus(_A)
class _H3cLicenseFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cLicenseFeatureName_Type.__name__=_D
_H3cLicenseFeatureName_Object=MibTableColumn
h3cLicenseFeatureName=_H3cLicenseFeatureName_Object((1,3,6,1,4,1,2011,10,2,145,2,3,1,1),_H3cLicenseFeatureName_Type())
h3cLicenseFeatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseFeatureName.setStatus(_A)
class _H3cLicenseFeatureState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notLicensed',1),('trialLicense',2),('formalLicense',3)))
_H3cLicenseFeatureState_Type.__name__=_E
_H3cLicenseFeatureState_Object=MibTableColumn
h3cLicenseFeatureState=_H3cLicenseFeatureState_Object((1,3,6,1,4,1,2011,10,2,145,2,3,1,2),_H3cLicenseFeatureState_Type())
h3cLicenseFeatureState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseFeatureState.setStatus(_A)
_H3cLicenseOpTable_Object=MibTable
h3cLicenseOpTable=_H3cLicenseOpTable_Object((1,3,6,1,4,1,2011,10,2,145,2,4))
if mibBuilder.loadTexts:h3cLicenseOpTable.setStatus(_A)
_H3cLicenseOpEntry_Object=MibTableRow
h3cLicenseOpEntry=_H3cLicenseOpEntry_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1))
h3cLicenseOpEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:h3cLicenseOpEntry.setStatus(_A)
_H3cLicenseOpIndex_Type=Unsigned32
_H3cLicenseOpIndex_Object=MibTableColumn
h3cLicenseOpIndex=_H3cLicenseOpIndex_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1,1),_H3cLicenseOpIndex_Type())
h3cLicenseOpIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLicenseOpIndex.setStatus(_A)
_H3cLicenseOpPhysicalIndex_Type=PhysicalIndexOrZero
_H3cLicenseOpPhysicalIndex_Object=MibTableColumn
h3cLicenseOpPhysicalIndex=_H3cLicenseOpPhysicalIndex_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1,2),_H3cLicenseOpPhysicalIndex_Type())
h3cLicenseOpPhysicalIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLicenseOpPhysicalIndex.setStatus(_A)
class _H3cLicenseOpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('compress',1),('delete',2),('installActivationFile',3),('installActivationKey',4),('installLicenseKey',5),('uninstallActivationFile',6),('uninstallActivationKey',7),('uninstallLicenseKey',8)))
_H3cLicenseOpType_Type.__name__=_E
_H3cLicenseOpType_Object=MibTableColumn
h3cLicenseOpType=_H3cLicenseOpType_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1,3),_H3cLicenseOpType_Type())
h3cLicenseOpType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLicenseOpType.setStatus(_A)
class _H3cLicenseOpString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseOpString_Type.__name__=_D
_H3cLicenseOpString_Object=MibTableColumn
h3cLicenseOpString=_H3cLicenseOpString_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1,4),_H3cLicenseOpString_Type())
h3cLicenseOpString.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLicenseOpString.setStatus(_A)
class _H3cLicenseOpNotifyEnable_Type(TruthValue):defaultValue=2
_H3cLicenseOpNotifyEnable_Type.__name__=_J
_H3cLicenseOpNotifyEnable_Object=MibTableColumn
h3cLicenseOpNotifyEnable=_H3cLicenseOpNotifyEnable_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1,5),_H3cLicenseOpNotifyEnable_Type())
h3cLicenseOpNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLicenseOpNotifyEnable.setStatus(_A)
_H3cLicenseOpRowStatus_Type=RowStatus
_H3cLicenseOpRowStatus_Object=MibTableColumn
h3cLicenseOpRowStatus=_H3cLicenseOpRowStatus_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1,6),_H3cLicenseOpRowStatus_Type())
h3cLicenseOpRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLicenseOpRowStatus.setStatus(_A)
class _H3cLicenseOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('opInProgress',1),('opSuccessful',2),('opFailed',3)))
_H3cLicenseOpState_Type.__name__=_E
_H3cLicenseOpState_Object=MibTableColumn
h3cLicenseOpState=_H3cLicenseOpState_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1,7),_H3cLicenseOpState_Type())
h3cLicenseOpState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseOpState.setStatus(_A)
class _H3cLicenseOpFailedReason_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cLicenseOpFailedReason_Type.__name__=_D
_H3cLicenseOpFailedReason_Object=MibTableColumn
h3cLicenseOpFailedReason=_H3cLicenseOpFailedReason_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1,8),_H3cLicenseOpFailedReason_Type())
h3cLicenseOpFailedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseOpFailedReason.setStatus(_A)
_H3cLicenseOpEndTime_Type=TimeTicks
_H3cLicenseOpEndTime_Object=MibTableColumn
h3cLicenseOpEndTime=_H3cLicenseOpEndTime_Object((1,3,6,1,4,1,2011,10,2,145,2,4,1,9),_H3cLicenseOpEndTime_Type())
h3cLicenseOpEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLicenseOpEndTime.setStatus(_A)
_H3cLicenseNotifications_ObjectIdentity=ObjectIdentity
h3cLicenseNotifications=_H3cLicenseNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,145,3))
_H3cLicenseNotificationPrefix_ObjectIdentity=ObjectIdentity
h3cLicenseNotificationPrefix=_H3cLicenseNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,145,3,0))
_H3cLicenseNotificationBindings_ObjectIdentity=ObjectIdentity
h3cLicenseNotificationBindings=_H3cLicenseNotificationBindings_ObjectIdentity((1,3,6,1,4,1,2011,10,2,145,3,1))
_H3cLicenseBindValidityPeriodRemaining_Type=Unsigned32
_H3cLicenseBindValidityPeriodRemaining_Object=MibScalar
h3cLicenseBindValidityPeriodRemaining=_H3cLicenseBindValidityPeriodRemaining_Object((1,3,6,1,4,1,2011,10,2,145,3,1,1),_H3cLicenseBindValidityPeriodRemaining_Type())
h3cLicenseBindValidityPeriodRemaining.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLicenseBindValidityPeriodRemaining.setStatus(_A)
if mibBuilder.loadTexts:h3cLicenseBindValidityPeriodRemaining.setUnits('days')
h3cLicenseOpCompletion=NotificationType((1,3,6,1,4,1,2011,10,2,145,3,0,1))
h3cLicenseOpCompletion.setObjects(*((_C,_L),(_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W)))
if mibBuilder.loadTexts:h3cLicenseOpCompletion.setStatus(_A)
h3cLicenseActivationFileLost=NotificationType((1,3,6,1,4,1,2011,10,2,145,3,0,2))
h3cLicenseActivationFileLost.setObjects(*((_C,_F),(_C,_M)))
if mibBuilder.loadTexts:h3cLicenseActivationFileLost.setStatus(_A)
h3cLicenseActivationFileRestored=NotificationType((1,3,6,1,4,1,2011,10,2,145,3,0,3))
h3cLicenseActivationFileRestored.setObjects(*((_C,_F),(_C,_M)))
if mibBuilder.loadTexts:h3cLicenseActivationFileRestored.setStatus(_A)
h3cLicenseExpired=NotificationType((1,3,6,1,4,1,2011,10,2,145,3,0,4))
h3cLicenseExpired.setObjects(*((_C,_I),(_C,_N)))
if mibBuilder.loadTexts:h3cLicenseExpired.setStatus(_A)
h3cLicenseExpireWarning=NotificationType((1,3,6,1,4,1,2011,10,2,145,3,0,5))
h3cLicenseExpireWarning.setObjects(*((_C,_I),(_C,_N),(_C,_X)))
if mibBuilder.loadTexts:h3cLicenseExpireWarning.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cLicense':h3cLicense,'h3cLicenseScalarObjects':h3cLicenseScalarObjects,'h3cLicenseNotifyEnable':h3cLicenseNotifyEnable,'h3cLicenseOpEntryMaxNum':h3cLicenseOpEntryMaxNum,'h3cLicenseNextFreeOpIndex':h3cLicenseNextFreeOpIndex,'h3cLicenseTables':h3cLicenseTables,'h3cLicenseDevInfoTable':h3cLicenseDevInfoTable,'h3cLicenseDevInfoEntry':h3cLicenseDevInfoEntry,_F:h3cLicensePhysicalIndex,'h3cLicenseSN':h3cLicenseSN,'h3cLicenseDeviceIDType':h3cLicenseDeviceIDType,'h3cLicenseDeviceID':h3cLicenseDeviceID,'h3cLicenseHardwareInfo':h3cLicenseHardwareInfo,'h3cLicenseMaxNum':h3cLicenseMaxNum,'h3cLicenseUsedNum':h3cLicenseUsedNum,'h3cLicenseRecyclableNum':h3cLicenseRecyclableNum,'h3cLicenseInstallType':h3cLicenseInstallType,'h3cLicenseFileStoragePath':h3cLicenseFileStoragePath,'h3cLicenseGeneralTable':h3cLicenseGeneralTable,'h3cLicenseGeneralEntry':h3cLicenseGeneralEntry,_R:h3cLicenseIndex,'h3cLicenseFeature':h3cLicenseFeature,'h3cLicenseProductDescr':h3cLicenseProductDescr,'h3cLicenseFileDescr':h3cLicenseFileDescr,'h3cLicenseState':h3cLicenseState,_M:h3cLicenseActivationFile,'h3cLicenseActivationKey':h3cLicenseActivationKey,'h3cLicenseLicenseKey':h3cLicenseLicenseKey,'h3cLicenseUninstActivationFile':h3cLicenseUninstActivationFile,'h3cLicenseUninstActivationKey':h3cLicenseUninstActivationKey,'h3cLicenseType':h3cLicenseType,'h3cLicenseInstalledTime':h3cLicenseInstalledTime,'h3cLicenseUninstalledTime':h3cLicenseUninstalledTime,'h3cLicenseDaysLeft':h3cLicenseDaysLeft,'h3cLicenseValidityStart':h3cLicenseValidityStart,'h3cLicenseValidityEnd':h3cLicenseValidityEnd,'h3cLicenseExpiredDays':h3cLicenseExpiredDays,'h3cLicenseCount':h3cLicenseCount,'h3cLicenseFeatureTable':h3cLicenseFeatureTable,'h3cLicenseFeatureEntry':h3cLicenseFeatureEntry,_I:h3cLicenseFeatureName,_N:h3cLicenseFeatureState,'h3cLicenseOpTable':h3cLicenseOpTable,'h3cLicenseOpEntry':h3cLicenseOpEntry,_L:h3cLicenseOpIndex,_S:h3cLicenseOpPhysicalIndex,_T:h3cLicenseOpType,_U:h3cLicenseOpString,'h3cLicenseOpNotifyEnable':h3cLicenseOpNotifyEnable,'h3cLicenseOpRowStatus':h3cLicenseOpRowStatus,_V:h3cLicenseOpState,_W:h3cLicenseOpFailedReason,'h3cLicenseOpEndTime':h3cLicenseOpEndTime,'h3cLicenseNotifications':h3cLicenseNotifications,'h3cLicenseNotificationPrefix':h3cLicenseNotificationPrefix,'h3cLicenseOpCompletion':h3cLicenseOpCompletion,'h3cLicenseActivationFileLost':h3cLicenseActivationFileLost,'h3cLicenseActivationFileRestored':h3cLicenseActivationFileRestored,'h3cLicenseExpired':h3cLicenseExpired,'h3cLicenseExpireWarning':h3cLicenseExpireWarning,'h3cLicenseNotificationBindings':h3cLicenseNotificationBindings,_X:h3cLicenseBindValidityPeriodRemaining})