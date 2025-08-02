if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2ConfigurationMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2ConfigurationMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2QosMib=ModuleIdentity((1,3,6,1,4,1,248,11,32))
if mibBuilder.loadTexts:hm2QosMib.setRevisions(('2011-03-16 00:00',))
_Hm2QosMibNotifications_ObjectIdentity=ObjectIdentity
hm2QosMibNotifications=_Hm2QosMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,32,0))
_Hm2QosMibObjects_ObjectIdentity=ObjectIdentity
hm2QosMibObjects=_Hm2QosMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,32,1))
_Hm2QosFirstGroup_ObjectIdentity=ObjectIdentity
hm2QosFirstGroup=_Hm2QosFirstGroup_ObjectIdentity((1,3,6,1,4,1,248,11,32,1,1))
_Hm2QosNextGroup_ObjectIdentity=ObjectIdentity
hm2QosNextGroup=_Hm2QosNextGroup_ObjectIdentity((1,3,6,1,4,1,248,11,32,1,2))
mibBuilder.exportSymbols('HM2-QOS-MIB',**{'hm2QosMib':hm2QosMib,'hm2QosMibNotifications':hm2QosMibNotifications,'hm2QosMibObjects':hm2QosMibObjects,'hm2QosFirstGroup':hm2QosFirstGroup,'hm2QosNextGroup':hm2QosNextGroup})