if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cARPEntry=ModuleIdentity((1,3,6,1,4,1,2011,10,2,168))
if mibBuilder.loadTexts:h3cARPEntry.setRevisions(('2017-03-14 00:00',))
_H3cARPEntryCountObjects_ObjectIdentity=ObjectIdentity
h3cARPEntryCountObjects=_H3cARPEntryCountObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,168,1))
_H3cARPEntryOpenFlowCount_Type=Counter32
_H3cARPEntryOpenFlowCount_Object=MibScalar
h3cARPEntryOpenFlowCount=_H3cARPEntryOpenFlowCount_Object((1,3,6,1,4,1,2011,10,2,168,1,1),_H3cARPEntryOpenFlowCount_Type())
h3cARPEntryOpenFlowCount.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cARPEntryOpenFlowCount.setStatus('current')
mibBuilder.exportSymbols('H3C-ARP-ENTRY-MIB',**{'h3cARPEntry':h3cARPEntry,'h3cARPEntryCountObjects':h3cARPEntryCountObjects,'h3cARPEntryOpenFlowCount':h3cARPEntryOpenFlowCount})