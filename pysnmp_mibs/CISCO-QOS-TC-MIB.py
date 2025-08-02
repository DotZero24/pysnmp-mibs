_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoQosTcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,573))
if mibBuilder.loadTexts:ciscoQosTcMIB.setRevisions(('2007-03-05 00:00','2006-09-18 12:00'))
class QosIpPrecedence(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class QosQueueNumber(TextualConvention,Unsigned32):status=_A
class QosThresholdNumber(TextualConvention,Unsigned32):status=_A
class QosMplsExpValue(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class QosMutationMapName(TextualConvention,OctetString):status=_A;displayHint='99a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,99))
class QosMutationMapNameOrEmpty(TextualConvention,OctetString):status=_A;displayHint='99a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
class QosPolicerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('microflow',1),('aggregate',2)))
mibBuilder.exportSymbols('CISCO-QOS-TC-MIB',**{'QosIpPrecedence':QosIpPrecedence,'QosQueueNumber':QosQueueNumber,'QosThresholdNumber':QosThresholdNumber,'QosMplsExpValue':QosMplsExpValue,'QosMutationMapName':QosMutationMapName,'QosMutationMapNameOrEmpty':QosMutationMapNameOrEmpty,'QosPolicerType':QosPolicerType,'ciscoQosTcMIB':ciscoQosTcMIB})