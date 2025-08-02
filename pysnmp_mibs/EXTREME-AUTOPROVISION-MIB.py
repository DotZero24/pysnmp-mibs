_I='extremeAutoProvisionConfigFileName'
_H='extremeAutoProvisionTFTPServer'
_G='extremeAutoProvisionGateway'
_F='extremeAutoProvisionIpAddress'
_E='extremeAutoProvisionResult'
_D='Integer32'
_C='accessible-for-notify'
_B='EXTREME-AUTOPROVISION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
extremeAutoProvision=ModuleIdentity((1,3,6,1,4,1,1916,1,40))
if mibBuilder.loadTexts:extremeAutoProvision.setRevisions(('2010-06-04 00:00',))
_ExtremeAutoProvisionGeneral_ObjectIdentity=ObjectIdentity
extremeAutoProvisionGeneral=_ExtremeAutoProvisionGeneral_ObjectIdentity((1,3,6,1,4,1,1916,1,40,1))
_ExtremeAutoProvisionConfig_Type=TruthValue
_ExtremeAutoProvisionConfig_Object=MibScalar
extremeAutoProvisionConfig=_ExtremeAutoProvisionConfig_Object((1,3,6,1,4,1,1916,1,40,1,1),_ExtremeAutoProvisionConfig_Type())
extremeAutoProvisionConfig.setMaxAccess('read-write')
if mibBuilder.loadTexts:extremeAutoProvisionConfig.setStatus(_A)
_ExtremeAutoProvisionNotificationObjects_ObjectIdentity=ObjectIdentity
extremeAutoProvisionNotificationObjects=_ExtremeAutoProvisionNotificationObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,40,2))
class _ExtremeAutoProvisionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalidConfigFileExtension',1),('tftpUnReachable',2),('fileNotExist',3),('success',4)))
_ExtremeAutoProvisionResult_Type.__name__=_D
_ExtremeAutoProvisionResult_Object=MibScalar
extremeAutoProvisionResult=_ExtremeAutoProvisionResult_Object((1,3,6,1,4,1,1916,1,40,2,1),_ExtremeAutoProvisionResult_Type())
extremeAutoProvisionResult.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeAutoProvisionResult.setStatus(_A)
_ExtremeAutoProvisionIpAddress_Type=IpAddress
_ExtremeAutoProvisionIpAddress_Object=MibScalar
extremeAutoProvisionIpAddress=_ExtremeAutoProvisionIpAddress_Object((1,3,6,1,4,1,1916,1,40,2,2),_ExtremeAutoProvisionIpAddress_Type())
extremeAutoProvisionIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeAutoProvisionIpAddress.setStatus(_A)
_ExtremeAutoProvisionGateway_Type=IpAddress
_ExtremeAutoProvisionGateway_Object=MibScalar
extremeAutoProvisionGateway=_ExtremeAutoProvisionGateway_Object((1,3,6,1,4,1,1916,1,40,2,3),_ExtremeAutoProvisionGateway_Type())
extremeAutoProvisionGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeAutoProvisionGateway.setStatus(_A)
_ExtremeAutoProvisionTFTPServer_Type=IpAddress
_ExtremeAutoProvisionTFTPServer_Object=MibScalar
extremeAutoProvisionTFTPServer=_ExtremeAutoProvisionTFTPServer_Object((1,3,6,1,4,1,1916,1,40,2,4),_ExtremeAutoProvisionTFTPServer_Type())
extremeAutoProvisionTFTPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeAutoProvisionTFTPServer.setStatus(_A)
_ExtremeAutoProvisionConfigFileName_Type=DisplayString
_ExtremeAutoProvisionConfigFileName_Object=MibScalar
extremeAutoProvisionConfigFileName=_ExtremeAutoProvisionConfigFileName_Object((1,3,6,1,4,1,1916,1,40,2,5),_ExtremeAutoProvisionConfigFileName_Type())
extremeAutoProvisionConfigFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeAutoProvisionConfigFileName.setStatus(_A)
_ExtremeAutoProvisionNotification_ObjectIdentity=ObjectIdentity
extremeAutoProvisionNotification=_ExtremeAutoProvisionNotification_ObjectIdentity((1,3,6,1,4,1,1916,1,40,3))
_ExtremeAutoProvisionTrapPrefix_ObjectIdentity=ObjectIdentity
extremeAutoProvisionTrapPrefix=_ExtremeAutoProvisionTrapPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,40,3,0))
extremeAutoProvisionStatus=NotificationType((1,3,6,1,4,1,1916,1,40,3,0,1))
extremeAutoProvisionStatus.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:extremeAutoProvisionStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extremeAutoProvision':extremeAutoProvision,'extremeAutoProvisionGeneral':extremeAutoProvisionGeneral,'extremeAutoProvisionConfig':extremeAutoProvisionConfig,'extremeAutoProvisionNotificationObjects':extremeAutoProvisionNotificationObjects,_E:extremeAutoProvisionResult,_F:extremeAutoProvisionIpAddress,_G:extremeAutoProvisionGateway,_H:extremeAutoProvisionTFTPServer,_I:extremeAutoProvisionConfigFileName,'extremeAutoProvisionNotification':extremeAutoProvisionNotification,'extremeAutoProvisionTrapPrefix':extremeAutoProvisionTrapPrefix,'extremeAutoProvisionStatus':extremeAutoProvisionStatus})