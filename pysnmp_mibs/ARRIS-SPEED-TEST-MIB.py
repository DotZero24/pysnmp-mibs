_F='arrisSpeedTestResultsIndex'
_E='ARRIS-SPEED-TEST-MIB'
_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProdIdCM,=mibBuilder.importSymbols('ARRIS-MIB','arrisProdIdCM')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeInterval','TimeStamp','TruthValue')
arrisSpeedTestMib=ModuleIdentity((1,3,6,1,4,1,4115,1,3,6))
if mibBuilder.loadTexts:arrisSpeedTestMib.setRevisions(('1911-08-09 00:00','1911-07-26 00:00','1910-07-16 00:00'))
_ArrisSpeedTestMibObjects_ObjectIdentity=ObjectIdentity
arrisSpeedTestMibObjects=_ArrisSpeedTestMibObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,3,6,1))
_ArrisSpeedTestConfig_ObjectIdentity=ObjectIdentity
arrisSpeedTestConfig=_ArrisSpeedTestConfig_ObjectIdentity((1,3,6,1,4,1,4115,1,3,6,1,1))
class _ArrisSpeedTestConfigDownlinkURL_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_ArrisSpeedTestConfigDownlinkURL_Type.__name__=_C
_ArrisSpeedTestConfigDownlinkURL_Object=MibScalar
arrisSpeedTestConfigDownlinkURL=_ArrisSpeedTestConfigDownlinkURL_Object((1,3,6,1,4,1,4115,1,3,6,1,1,1),_ArrisSpeedTestConfigDownlinkURL_Type())
arrisSpeedTestConfigDownlinkURL.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisSpeedTestConfigDownlinkURL.setStatus(_A)
class _ArrisSpeedTestConfigUplinkURL_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_ArrisSpeedTestConfigUplinkURL_Type.__name__=_C
_ArrisSpeedTestConfigUplinkURL_Object=MibScalar
arrisSpeedTestConfigUplinkURL=_ArrisSpeedTestConfigUplinkURL_Object((1,3,6,1,4,1,4115,1,3,6,1,1,2),_ArrisSpeedTestConfigUplinkURL_Type())
arrisSpeedTestConfigUplinkURL.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisSpeedTestConfigUplinkURL.setStatus(_A)
_ArrisSpeedTestConfigEndUserGui_Type=TruthValue
_ArrisSpeedTestConfigEndUserGui_Object=MibScalar
arrisSpeedTestConfigEndUserGui=_ArrisSpeedTestConfigEndUserGui_Object((1,3,6,1,4,1,4115,1,3,6,1,1,3),_ArrisSpeedTestConfigEndUserGui_Type())
arrisSpeedTestConfigEndUserGui.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisSpeedTestConfigEndUserGui.setStatus(_A)
_ArrisSpeedTestConfigSyslogReports_Type=TruthValue
_ArrisSpeedTestConfigSyslogReports_Object=MibScalar
arrisSpeedTestConfigSyslogReports=_ArrisSpeedTestConfigSyslogReports_Object((1,3,6,1,4,1,4115,1,3,6,1,1,4),_ArrisSpeedTestConfigSyslogReports_Type())
arrisSpeedTestConfigSyslogReports.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisSpeedTestConfigSyslogReports.setStatus(_A)
_ArrisSpeedTestConfigCpeAccess_Type=TruthValue
_ArrisSpeedTestConfigCpeAccess_Object=MibScalar
arrisSpeedTestConfigCpeAccess=_ArrisSpeedTestConfigCpeAccess_Object((1,3,6,1,4,1,4115,1,3,6,1,1,5),_ArrisSpeedTestConfigCpeAccess_Type())
arrisSpeedTestConfigCpeAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisSpeedTestConfigCpeAccess.setStatus(_A)
class _ArrisSpeedTestConfigStartStopTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('stopTest',0),('startDownlinkTest',1),('startUplinkTest',2),('startDownlinkUplinkTest',3)))
_ArrisSpeedTestConfigStartStopTest_Type.__name__=_D
_ArrisSpeedTestConfigStartStopTest_Object=MibScalar
arrisSpeedTestConfigStartStopTest=_ArrisSpeedTestConfigStartStopTest_Object((1,3,6,1,4,1,4115,1,3,6,1,1,6),_ArrisSpeedTestConfigStartStopTest_Type())
arrisSpeedTestConfigStartStopTest.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisSpeedTestConfigStartStopTest.setStatus(_A)
_ArrisSpeedTestResultsTable_Object=MibTable
arrisSpeedTestResultsTable=_ArrisSpeedTestResultsTable_Object((1,3,6,1,4,1,4115,1,3,6,1,2))
if mibBuilder.loadTexts:arrisSpeedTestResultsTable.setStatus(_A)
_ArrisSpeedTestResultsEntry_Object=MibTableRow
arrisSpeedTestResultsEntry=_ArrisSpeedTestResultsEntry_Object((1,3,6,1,4,1,4115,1,3,6,1,2,1))
arrisSpeedTestResultsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:arrisSpeedTestResultsEntry.setStatus(_A)
class _ArrisSpeedTestResultsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ArrisSpeedTestResultsIndex_Type.__name__=_D
_ArrisSpeedTestResultsIndex_Object=MibTableColumn
arrisSpeedTestResultsIndex=_ArrisSpeedTestResultsIndex_Object((1,3,6,1,4,1,4115,1,3,6,1,2,1,1),_ArrisSpeedTestResultsIndex_Type())
arrisSpeedTestResultsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:arrisSpeedTestResultsIndex.setStatus(_A)
class _ArrisSpeedTestResultsStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_ArrisSpeedTestResultsStatus_Type.__name__=_C
_ArrisSpeedTestResultsStatus_Object=MibTableColumn
arrisSpeedTestResultsStatus=_ArrisSpeedTestResultsStatus_Object((1,3,6,1,4,1,4115,1,3,6,1,2,1,2),_ArrisSpeedTestResultsStatus_Type())
arrisSpeedTestResultsStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:arrisSpeedTestResultsStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'arrisSpeedTestMib':arrisSpeedTestMib,'arrisSpeedTestMibObjects':arrisSpeedTestMibObjects,'arrisSpeedTestConfig':arrisSpeedTestConfig,'arrisSpeedTestConfigDownlinkURL':arrisSpeedTestConfigDownlinkURL,'arrisSpeedTestConfigUplinkURL':arrisSpeedTestConfigUplinkURL,'arrisSpeedTestConfigEndUserGui':arrisSpeedTestConfigEndUserGui,'arrisSpeedTestConfigSyslogReports':arrisSpeedTestConfigSyslogReports,'arrisSpeedTestConfigCpeAccess':arrisSpeedTestConfigCpeAccess,'arrisSpeedTestConfigStartStopTest':arrisSpeedTestConfigStartStopTest,'arrisSpeedTestResultsTable':arrisSpeedTestResultsTable,'arrisSpeedTestResultsEntry':arrisSpeedTestResultsEntry,_F:arrisSpeedTestResultsIndex,'arrisSpeedTestResultsStatus':arrisSpeedTestResultsStatus})