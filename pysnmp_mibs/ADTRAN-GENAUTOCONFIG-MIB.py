_Z='adGenAutoConfigTimeoutAlmSeverity'
_Y='adGenAutoConfigLastFailureReason'
_X='adGenAutoConfigFirmwareDefinitionFilename'
_W='adGenAutoConfigBaseConfigFilename'
_V='adGenAutoConfigUnitConfigFilename'
_U='adGenAutoConfigTempConfigFilename'
_T='adGenAutoConfigGroupName'
_S='adGenAutoConfigFilename'
_R='adGenAutoConfigFailureAlmSeverity'
_Q='critical'
_P='disabled'
_O='adGenAutoConfigLastFailureFilename'
_N='adGenAutoConfigHostIPv6'
_M='adGenAutoConfigHostIPv4'
_L='sysName'
_K='SNMPv2-MIB'
_J='adTrapInformSeqNum'
_I='ADTRAN-GENTRAPINFORM-MIB'
_H='adGenSlotProdSwVersion'
_G='adGenSlotProdPartNumber'
_F='Unsigned32'
_E='Integer32'
_D='ADTRAN-GENSLOT-MIB'
_C='ADTRAN-GENAUTOCONFIG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotProdPartNumber,adGenSlotProdSwVersion=mibBuilder.importSymbols(_D,_G,_H)
adTrapInformSeqNum,=mibBuilder.importSymbols(_I,_J)
adGenAutoConfig,adGenAutoConfigID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenAutoConfig','adGenAutoConfigID')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_K,_L)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
adGenAutoConfigMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,59,1))
if mibBuilder.loadTexts:adGenAutoConfigMIB.setRevisions(('2014-10-13 00:00',))
_AdGenAutoConfigEvents_ObjectIdentity=ObjectIdentity
adGenAutoConfigEvents=_AdGenAutoConfigEvents_ObjectIdentity((1,3,6,1,4,1,664,5,70,59,0))
_AdGenAutoConfigStatus_ObjectIdentity=ObjectIdentity
adGenAutoConfigStatus=_AdGenAutoConfigStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,59,1))
_AdGenAutoConfigEnabled_Type=TruthValue
_AdGenAutoConfigEnabled_Object=MibScalar
adGenAutoConfigEnabled=_AdGenAutoConfigEnabled_Object((1,3,6,1,4,1,664,5,70,59,1,1),_AdGenAutoConfigEnabled_Type())
adGenAutoConfigEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigEnabled.setStatus(_A)
_AdGenAutoConfigHostIPv4_Type=InetAddressIPv4
_AdGenAutoConfigHostIPv4_Object=MibScalar
adGenAutoConfigHostIPv4=_AdGenAutoConfigHostIPv4_Object((1,3,6,1,4,1,664,5,70,59,1,2),_AdGenAutoConfigHostIPv4_Type())
adGenAutoConfigHostIPv4.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigHostIPv4.setStatus(_A)
_AdGenAutoConfigHostIPv6_Type=InetAddressIPv6
_AdGenAutoConfigHostIPv6_Object=MibScalar
adGenAutoConfigHostIPv6=_AdGenAutoConfigHostIPv6_Object((1,3,6,1,4,1,664,5,70,59,1,3),_AdGenAutoConfigHostIPv6_Type())
adGenAutoConfigHostIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigHostIPv6.setStatus(_A)
_AdGenAutoConfigFilename_Type=DisplayString
_AdGenAutoConfigFilename_Object=MibScalar
adGenAutoConfigFilename=_AdGenAutoConfigFilename_Object((1,3,6,1,4,1,664,5,70,59,1,4),_AdGenAutoConfigFilename_Type())
adGenAutoConfigFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigFilename.setStatus(_A)
_AdGenAutoConfigGroupName_Type=DisplayString
_AdGenAutoConfigGroupName_Object=MibScalar
adGenAutoConfigGroupName=_AdGenAutoConfigGroupName_Object((1,3,6,1,4,1,664,5,70,59,1,5),_AdGenAutoConfigGroupName_Type())
adGenAutoConfigGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigGroupName.setStatus(_A)
_AdGenAutoConfigTempConfigFilename_Type=DisplayString
_AdGenAutoConfigTempConfigFilename_Object=MibScalar
adGenAutoConfigTempConfigFilename=_AdGenAutoConfigTempConfigFilename_Object((1,3,6,1,4,1,664,5,70,59,1,6),_AdGenAutoConfigTempConfigFilename_Type())
adGenAutoConfigTempConfigFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigTempConfigFilename.setStatus(_A)
_AdGenAutoConfigUnitConfigFilename_Type=DisplayString
_AdGenAutoConfigUnitConfigFilename_Object=MibScalar
adGenAutoConfigUnitConfigFilename=_AdGenAutoConfigUnitConfigFilename_Object((1,3,6,1,4,1,664,5,70,59,1,7),_AdGenAutoConfigUnitConfigFilename_Type())
adGenAutoConfigUnitConfigFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigUnitConfigFilename.setStatus(_A)
_AdGenAutoConfigBaseConfigFilename_Type=DisplayString
_AdGenAutoConfigBaseConfigFilename_Object=MibScalar
adGenAutoConfigBaseConfigFilename=_AdGenAutoConfigBaseConfigFilename_Object((1,3,6,1,4,1,664,5,70,59,1,8),_AdGenAutoConfigBaseConfigFilename_Type())
adGenAutoConfigBaseConfigFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigBaseConfigFilename.setStatus(_A)
_AdGenAutoConfigFirmwareDefinitionFilename_Type=DisplayString
_AdGenAutoConfigFirmwareDefinitionFilename_Object=MibScalar
adGenAutoConfigFirmwareDefinitionFilename=_AdGenAutoConfigFirmwareDefinitionFilename_Object((1,3,6,1,4,1,664,5,70,59,1,9),_AdGenAutoConfigFirmwareDefinitionFilename_Type())
adGenAutoConfigFirmwareDefinitionFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigFirmwareDefinitionFilename.setStatus(_A)
class _AdGenAutoConfigRetryCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AdGenAutoConfigRetryCount_Type.__name__=_F
_AdGenAutoConfigRetryCount_Object=MibScalar
adGenAutoConfigRetryCount=_AdGenAutoConfigRetryCount_Object((1,3,6,1,4,1,664,5,70,59,1,10),_AdGenAutoConfigRetryCount_Type())
adGenAutoConfigRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigRetryCount.setStatus(_A)
class _AdGenAutoConfigPollingInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2592000))
_AdGenAutoConfigPollingInterval_Type.__name__=_F
_AdGenAutoConfigPollingInterval_Object=MibScalar
adGenAutoConfigPollingInterval=_AdGenAutoConfigPollingInterval_Object((1,3,6,1,4,1,664,5,70,59,1,11),_AdGenAutoConfigPollingInterval_Type())
adGenAutoConfigPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigPollingInterval.setStatus(_A)
class _AdGenAutoConfigProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),('ftp',2),('sftp',3)))
_AdGenAutoConfigProtocol_Type.__name__=_E
_AdGenAutoConfigProtocol_Object=MibScalar
adGenAutoConfigProtocol=_AdGenAutoConfigProtocol_Object((1,3,6,1,4,1,664,5,70,59,1,12),_AdGenAutoConfigProtocol_Type())
adGenAutoConfigProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigProtocol.setStatus(_A)
class _AdGenAutoConfigProtocolPortSFTP_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AdGenAutoConfigProtocolPortSFTP_Type.__name__=_F
_AdGenAutoConfigProtocolPortSFTP_Object=MibScalar
adGenAutoConfigProtocolPortSFTP=_AdGenAutoConfigProtocolPortSFTP_Object((1,3,6,1,4,1,664,5,70,59,1,13),_AdGenAutoConfigProtocolPortSFTP_Type())
adGenAutoConfigProtocolPortSFTP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigProtocolPortSFTP.setStatus(_A)
_AdGenAutoConfigLastFailureFilename_Type=DisplayString
_AdGenAutoConfigLastFailureFilename_Object=MibScalar
adGenAutoConfigLastFailureFilename=_AdGenAutoConfigLastFailureFilename_Object((1,3,6,1,4,1,664,5,70,59,1,14),_AdGenAutoConfigLastFailureFilename_Type())
adGenAutoConfigLastFailureFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigLastFailureFilename.setStatus(_A)
_AdGenAutoConfigLastFailureReason_Type=DisplayString
_AdGenAutoConfigLastFailureReason_Object=MibScalar
adGenAutoConfigLastFailureReason=_AdGenAutoConfigLastFailureReason_Object((1,3,6,1,4,1,664,5,70,59,1,15),_AdGenAutoConfigLastFailureReason_Type())
adGenAutoConfigLastFailureReason.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigLastFailureReason.setStatus(_A)
_AdGenAutoConfigCurrentStatus_Type=DisplayString
_AdGenAutoConfigCurrentStatus_Object=MibScalar
adGenAutoConfigCurrentStatus=_AdGenAutoConfigCurrentStatus_Object((1,3,6,1,4,1,664,5,70,59,1,16),_AdGenAutoConfigCurrentStatus_Type())
adGenAutoConfigCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigCurrentStatus.setStatus(_A)
class _AdGenAutoConfigFailureAlmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),('info',2),('alert',3),('minor',4),('major',5),(_Q,6)))
_AdGenAutoConfigFailureAlmSeverity_Type.__name__=_E
_AdGenAutoConfigFailureAlmSeverity_Object=MibScalar
adGenAutoConfigFailureAlmSeverity=_AdGenAutoConfigFailureAlmSeverity_Object((1,3,6,1,4,1,664,5,70,59,1,17),_AdGenAutoConfigFailureAlmSeverity_Type())
adGenAutoConfigFailureAlmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigFailureAlmSeverity.setStatus(_A)
class _AdGenAutoConfigTimeoutAlmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),('info',2),('alert',3),('minor',4),('major',5),(_Q,6)))
_AdGenAutoConfigTimeoutAlmSeverity_Type.__name__=_E
_AdGenAutoConfigTimeoutAlmSeverity_Object=MibScalar
adGenAutoConfigTimeoutAlmSeverity=_AdGenAutoConfigTimeoutAlmSeverity_Object((1,3,6,1,4,1,664,5,70,59,1,18),_AdGenAutoConfigTimeoutAlmSeverity_Type())
adGenAutoConfigTimeoutAlmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAutoConfigTimeoutAlmSeverity.setStatus(_A)
_AdGenAutoConfigProvisioning_ObjectIdentity=ObjectIdentity
adGenAutoConfigProvisioning=_AdGenAutoConfigProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,59,2))
class _AdGenAutoConfigRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restart',1))
_AdGenAutoConfigRestart_Type.__name__=_E
_AdGenAutoConfigRestart_Object=MibScalar
adGenAutoConfigRestart=_AdGenAutoConfigRestart_Object((1,3,6,1,4,1,664,5,70,59,2,1),_AdGenAutoConfigRestart_Type())
adGenAutoConfigRestart.setMaxAccess('read-write')
if mibBuilder.loadTexts:adGenAutoConfigRestart.setStatus(_A)
adGenAutoConfigFailureAlm=NotificationType((1,3,6,1,4,1,664,5,70,59,0,1))
adGenAutoConfigFailureAlm.setObjects(*((_I,_J),(_K,_L),(_C,_R),(_D,_G),(_D,_H),(_C,_M),(_C,_N),(_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X),(_C,_O),(_C,_Y)))
if mibBuilder.loadTexts:adGenAutoConfigFailureAlm.setStatus(_A)
adGenAutoConfigTimeoutAlm=NotificationType((1,3,6,1,4,1,664,5,70,59,0,2))
adGenAutoConfigTimeoutAlm.setObjects(*((_I,_J),(_K,_L),(_C,_Z),(_D,_G),(_D,_H),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:adGenAutoConfigTimeoutAlm.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'adGenAutoConfigEvents':adGenAutoConfigEvents,'adGenAutoConfigFailureAlm':adGenAutoConfigFailureAlm,'adGenAutoConfigTimeoutAlm':adGenAutoConfigTimeoutAlm,'adGenAutoConfigStatus':adGenAutoConfigStatus,'adGenAutoConfigEnabled':adGenAutoConfigEnabled,_M:adGenAutoConfigHostIPv4,_N:adGenAutoConfigHostIPv6,_S:adGenAutoConfigFilename,_T:adGenAutoConfigGroupName,_U:adGenAutoConfigTempConfigFilename,_V:adGenAutoConfigUnitConfigFilename,_W:adGenAutoConfigBaseConfigFilename,_X:adGenAutoConfigFirmwareDefinitionFilename,'adGenAutoConfigRetryCount':adGenAutoConfigRetryCount,'adGenAutoConfigPollingInterval':adGenAutoConfigPollingInterval,'adGenAutoConfigProtocol':adGenAutoConfigProtocol,'adGenAutoConfigProtocolPortSFTP':adGenAutoConfigProtocolPortSFTP,_O:adGenAutoConfigLastFailureFilename,_Y:adGenAutoConfigLastFailureReason,'adGenAutoConfigCurrentStatus':adGenAutoConfigCurrentStatus,_R:adGenAutoConfigFailureAlmSeverity,_Z:adGenAutoConfigTimeoutAlmSeverity,'adGenAutoConfigProvisioning':adGenAutoConfigProvisioning,'adGenAutoConfigRestart':adGenAutoConfigRestart,'adGenAutoConfigMIB':adGenAutoConfigMIB})