if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cLocAAASvr=ModuleIdentity((1,3,6,1,4,1,2011,10,2,141))
if mibBuilder.loadTexts:h3cLocAAASvr.setRevisions(('2013-07-06 09:45',))
_H3cLocAAASvrControl_ObjectIdentity=ObjectIdentity
h3cLocAAASvrControl=_H3cLocAAASvrControl_ObjectIdentity((1,3,6,1,4,1,2011,10,2,141,1))
_H3cLocAAASvrTables_ObjectIdentity=ObjectIdentity
h3cLocAAASvrTables=_H3cLocAAASvrTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,141,2))
_H3cLocAAASvrTrap_ObjectIdentity=ObjectIdentity
h3cLocAAASvrTrap=_H3cLocAAASvrTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,141,3))
_H3cLocAAASvrTrapPrex_ObjectIdentity=ObjectIdentity
h3cLocAAASvrTrapPrex=_H3cLocAAASvrTrapPrex_ObjectIdentity((1,3,6,1,4,1,2011,10,2,141,3,0))
h3cLocAAASvrBillExportFailed=NotificationType((1,3,6,1,4,1,2011,10,2,141,3,0,1))
if mibBuilder.loadTexts:h3cLocAAASvrBillExportFailed.setStatus('current')
mibBuilder.exportSymbols('H3C-LOCAL-AAA-SERVER-MIB',**{'h3cLocAAASvr':h3cLocAAASvr,'h3cLocAAASvrControl':h3cLocAAASvrControl,'h3cLocAAASvrTables':h3cLocAAASvrTables,'h3cLocAAASvrTrap':h3cLocAAASvrTrap,'h3cLocAAASvrTrapPrex':h3cLocAAASvrTrapPrex,'h3cLocAAASvrBillExportFailed':h3cLocAAASvrBillExportFailed})