_D='critical'
_C='other'
_B='unknown'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwSystem,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwSystem')
vmwTcMIB=ModuleIdentity((1,3,6,1,4,1,6876,1,11))
if mibBuilder.loadTexts:vmwTcMIB.setRevisions(('2009-09-05 00:00','2007-12-27 00:00'))
class VmwSubsystemTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_B,1),('chassis',2),('powerSupply',3),('fan',4),('cpu',5),('memory',6),('battery',7),('temperatureSensor',8),('raidController',9),('voltage',10)))
class VmwCIMAlertTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_C,1),('communications',2),('qos',3),('processingError',4),('deviceAlert',5),('environmentalAlert',6),('modelChange',7),('securityAlert',8)))
class VmwCIMAlertFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_B,0),(_C,1),('cimObjectPath',2)))
class VmwSubsystemStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_B,1),('normal',2),('marginal',3),(_D,4),('failed',5)))
class VmwCIMSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_B,0),(_C,1),('information',2),('warning',3),('minor',4),('major',5),(_D,6),('fatal',7)))
class VmwCimName(TextualConvention,OctetString):status=_A;displayHint='256a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class VmwConnectedState(TextualConvention,OctetString):status=_A;displayHint='7a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,7))
class VmwLongDisplayString(TextualConvention,OctetString):status=_A;displayHint='1a'
class VmwLongSnmpAdminString(TextualConvention,OctetString):status=_A;displayHint='4096t'
class VmwUnixAbsFilePath(TextualConvention,OctetString):status=_A;displayHint='1024a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
mibBuilder.exportSymbols('VMWARE-TC-MIB',**{'VmwSubsystemTypes':VmwSubsystemTypes,'VmwCIMAlertTypes':VmwCIMAlertTypes,'VmwCIMAlertFormat':VmwCIMAlertFormat,'VmwSubsystemStatus':VmwSubsystemStatus,'VmwCIMSeverity':VmwCIMSeverity,'VmwCimName':VmwCimName,'VmwConnectedState':VmwConnectedState,'VmwLongDisplayString':VmwLongDisplayString,'VmwLongSnmpAdminString':VmwLongSnmpAdminString,'VmwUnixAbsFilePath':VmwUnixAbsFilePath,'vmwTcMIB':vmwTcMIB})