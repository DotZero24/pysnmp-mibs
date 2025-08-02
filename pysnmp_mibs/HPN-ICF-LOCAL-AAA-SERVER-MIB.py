if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfLocAAASvr=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,141))
if mibBuilder.loadTexts:hpnicfLocAAASvr.setRevisions(('2013-07-06 09:45',))
_HpnicfLocAAASvrControl_ObjectIdentity=ObjectIdentity
hpnicfLocAAASvrControl=_HpnicfLocAAASvrControl_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,141,1))
_HpnicfLocAAASvrTables_ObjectIdentity=ObjectIdentity
hpnicfLocAAASvrTables=_HpnicfLocAAASvrTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,141,2))
_HpnicfLocAAASvrTrap_ObjectIdentity=ObjectIdentity
hpnicfLocAAASvrTrap=_HpnicfLocAAASvrTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,141,3))
_HpnicfLocAAASvrTrapPrex_ObjectIdentity=ObjectIdentity
hpnicfLocAAASvrTrapPrex=_HpnicfLocAAASvrTrapPrex_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,141,3,0))
hpnicfLocAAASvrBillExportFailed=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,141,3,0,1))
if mibBuilder.loadTexts:hpnicfLocAAASvrBillExportFailed.setStatus('current')
mibBuilder.exportSymbols('HPN-ICF-LOCAL-AAA-SERVER-MIB',**{'hpnicfLocAAASvr':hpnicfLocAAASvr,'hpnicfLocAAASvrControl':hpnicfLocAAASvrControl,'hpnicfLocAAASvrTables':hpnicfLocAAASvrTables,'hpnicfLocAAASvrTrap':hpnicfLocAAASvrTrap,'hpnicfLocAAASvrTrapPrex':hpnicfLocAAASvrTrapPrex,'hpnicfLocAAASvrBillExportFailed':hpnicfLocAAASvrBillExportFailed})