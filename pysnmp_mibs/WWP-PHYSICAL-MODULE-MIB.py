_F='OctetString'
_E='Unsigned32'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'MacAddress','PhysAddress','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpPhyModuleMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,3))
if mibBuilder.loadTexts:wwpPhyModuleMIB.setRevisions(('2001-04-03 17:00',))
_WwpPhyModuleMIBObjects_ObjectIdentity=ObjectIdentity
wwpPhyModuleMIBObjects=_WwpPhyModuleMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,3,1))
_WwpPhyModuleInfo_ObjectIdentity=ObjectIdentity
wwpPhyModuleInfo=_WwpPhyModuleInfo_ObjectIdentity((1,3,6,1,4,1,6141,2,3,1,1))
class _WwpPhyModSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpPhyModSerialNum_Type.__name__=_C
_WwpPhyModSerialNum_Object=MibScalar
wwpPhyModSerialNum=_WwpPhyModSerialNum_Object((1,3,6,1,4,1,6141,2,3,1,1,1),_WwpPhyModSerialNum_Type())
wwpPhyModSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModSerialNum.setStatus(_A)
class _WwpPhyModBoardRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpPhyModBoardRevision_Type.__name__=_C
_WwpPhyModBoardRevision_Object=MibScalar
wwpPhyModBoardRevision=_WwpPhyModBoardRevision_Object((1,3,6,1,4,1,6141,2,3,1,1,2),_WwpPhyModBoardRevision_Type())
wwpPhyModBoardRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModBoardRevision.setStatus(_A)
class _WwpPhyModNumResets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpPhyModNumResets_Type.__name__=_E
_WwpPhyModNumResets_Object=MibScalar
wwpPhyModNumResets=_WwpPhyModNumResets_Object((1,3,6,1,4,1,6141,2,3,1,1,3),_WwpPhyModNumResets_Type())
wwpPhyModNumResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModNumResets.setStatus(_A)
_WwpPhyModFwVer_Type=DisplayString
_WwpPhyModFwVer_Object=MibScalar
wwpPhyModFwVer=_WwpPhyModFwVer_Object((1,3,6,1,4,1,6141,2,3,1,1,4),_WwpPhyModFwVer_Type())
wwpPhyModFwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModFwVer.setStatus(_A)
class _WwpPhyModAppVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpPhyModAppVer_Type.__name__=_C
_WwpPhyModAppVer_Object=MibScalar
wwpPhyModAppVer=_WwpPhyModAppVer_Object((1,3,6,1,4,1,6141,2,3,1,1,5),_WwpPhyModAppVer_Type())
wwpPhyModAppVer.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModAppVer.setStatus(_A)
_WwpPhyModPostResults_Type=DisplayString
_WwpPhyModPostResults_Object=MibScalar
wwpPhyModPostResults=_WwpPhyModPostResults_Object((1,3,6,1,4,1,6141,2,3,1,1,6),_WwpPhyModPostResults_Type())
wwpPhyModPostResults.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModPostResults.setStatus(_A)
class _WwpPhyModPostCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpPhyModPostCode_Type.__name__=_E
_WwpPhyModPostCode_Object=MibScalar
wwpPhyModPostCode=_WwpPhyModPostCode_Object((1,3,6,1,4,1,6141,2,3,1,1,7),_WwpPhyModPostCode_Type())
wwpPhyModPostCode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModPostCode.setStatus(_A)
_WwpPhyModBootLoaderVer_Type=DisplayString
_WwpPhyModBootLoaderVer_Object=MibScalar
wwpPhyModBootLoaderVer=_WwpPhyModBootLoaderVer_Object((1,3,6,1,4,1,6141,2,3,1,1,8),_WwpPhyModBootLoaderVer_Type())
wwpPhyModBootLoaderVer.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModBootLoaderVer.setStatus(_A)
_WwpPhyModMfgDate_Type=DateAndTime
_WwpPhyModMfgDate_Object=MibScalar
wwpPhyModMfgDate=_WwpPhyModMfgDate_Object((1,3,6,1,4,1,6141,2,3,1,1,9),_WwpPhyModMfgDate_Type())
wwpPhyModMfgDate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModMfgDate.setStatus(_A)
_WwpPhyModBoardType_Type=DisplayString
_WwpPhyModBoardType_Object=MibScalar
wwpPhyModBoardType=_WwpPhyModBoardType_Object((1,3,6,1,4,1,6141,2,3,1,1,10),_WwpPhyModBoardType_Type())
wwpPhyModBoardType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModBoardType.setStatus(_A)
class _WwpPhyModMktDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpPhyModMktDesc_Type.__name__=_F
_WwpPhyModMktDesc_Object=MibScalar
wwpPhyModMktDesc=_WwpPhyModMktDesc_Object((1,3,6,1,4,1,6141,2,3,1,1,11),_WwpPhyModMktDesc_Type())
wwpPhyModMktDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModMktDesc.setStatus(_A)
_WwpPhyModuleRebootAttr_ObjectIdentity=ObjectIdentity
wwpPhyModuleRebootAttr=_WwpPhyModuleRebootAttr_ObjectIdentity((1,3,6,1,4,1,6141,2,3,1,2))
class _WwpPhyModRebootOperation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('reboot',1),('rebootReinit',2),('rebootDefault',3)))
_WwpPhyModRebootOperation_Type.__name__=_D
_WwpPhyModRebootOperation_Object=MibScalar
wwpPhyModRebootOperation=_WwpPhyModRebootOperation_Object((1,3,6,1,4,1,6141,2,3,1,2,1),_WwpPhyModRebootOperation_Type())
wwpPhyModRebootOperation.setMaxAccess('read-write')
if mibBuilder.loadTexts:wwpPhyModRebootOperation.setStatus(_A)
_WwpPhyModLastRebootTime_Type=DateAndTime
_WwpPhyModLastRebootTime_Object=MibScalar
wwpPhyModLastRebootTime=_WwpPhyModLastRebootTime_Object((1,3,6,1,4,1,6141,2,3,1,2,2),_WwpPhyModLastRebootTime_Type())
wwpPhyModLastRebootTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModLastRebootTime.setStatus(_A)
class _WwpPhyModLastRebootReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('hostRequest',1),('pwrFail',2),('unknown',3),('softwareForced',4)))
_WwpPhyModLastRebootReason_Type.__name__=_D
_WwpPhyModLastRebootReason_Object=MibScalar
wwpPhyModLastRebootReason=_WwpPhyModLastRebootReason_Object((1,3,6,1,4,1,6141,2,3,1,2,3),_WwpPhyModLastRebootReason_Type())
wwpPhyModLastRebootReason.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPhyModLastRebootReason.setStatus(_A)
_WwpPhyModuleMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpPhyModuleMIBNotificationPrefix=_WwpPhyModuleMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,3,2))
_WwpPhyModuleMIBNotifications_ObjectIdentity=ObjectIdentity
wwpPhyModuleMIBNotifications=_WwpPhyModuleMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,3,2,0))
_WwpPhyModuleMIBConformance_ObjectIdentity=ObjectIdentity
wwpPhyModuleMIBConformance=_WwpPhyModuleMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,3,3))
_WwpPhyModuleMIBCompliances_ObjectIdentity=ObjectIdentity
wwpPhyModuleMIBCompliances=_WwpPhyModuleMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,3,3,1))
_WwpPhyModuleMIBGroups_ObjectIdentity=ObjectIdentity
wwpPhyModuleMIBGroups=_WwpPhyModuleMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,3,3,2))
mibBuilder.exportSymbols('WWP-PHYSICAL-MODULE-MIB',**{'wwpPhyModuleMIB':wwpPhyModuleMIB,'wwpPhyModuleMIBObjects':wwpPhyModuleMIBObjects,'wwpPhyModuleInfo':wwpPhyModuleInfo,'wwpPhyModSerialNum':wwpPhyModSerialNum,'wwpPhyModBoardRevision':wwpPhyModBoardRevision,'wwpPhyModNumResets':wwpPhyModNumResets,'wwpPhyModFwVer':wwpPhyModFwVer,'wwpPhyModAppVer':wwpPhyModAppVer,'wwpPhyModPostResults':wwpPhyModPostResults,'wwpPhyModPostCode':wwpPhyModPostCode,'wwpPhyModBootLoaderVer':wwpPhyModBootLoaderVer,'wwpPhyModMfgDate':wwpPhyModMfgDate,'wwpPhyModBoardType':wwpPhyModBoardType,'wwpPhyModMktDesc':wwpPhyModMktDesc,'wwpPhyModuleRebootAttr':wwpPhyModuleRebootAttr,'wwpPhyModRebootOperation':wwpPhyModRebootOperation,'wwpPhyModLastRebootTime':wwpPhyModLastRebootTime,'wwpPhyModLastRebootReason':wwpPhyModLastRebootReason,'wwpPhyModuleMIBNotificationPrefix':wwpPhyModuleMIBNotificationPrefix,'wwpPhyModuleMIBNotifications':wwpPhyModuleMIBNotifications,'wwpPhyModuleMIBConformance':wwpPhyModuleMIBConformance,'wwpPhyModuleMIBCompliances':wwpPhyModuleMIBCompliances,'wwpPhyModuleMIBGroups':wwpPhyModuleMIBGroups})