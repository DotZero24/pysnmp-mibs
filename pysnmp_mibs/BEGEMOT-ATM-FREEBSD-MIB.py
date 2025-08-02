_C='begemotAtmNgIfEntry'
_B='BEGEMOT-ATM-FREEBSD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemotAtmIfEntry,begemotAtmSysGroup=mibBuilder.importSymbols('BEGEMOT-ATM-MIB','begemotAtmIfEntry','begemotAtmSysGroup')
NgNodeIdOrZero,=mibBuilder.importSymbols('BEGEMOT-NETGRAPH-MIB','NgNodeIdOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
begemotAtmFreeBSDGroup=ModuleIdentity((1,3,6,1,4,1,12325,1,101,1,4,1))
_BegemotAtmNgGroup_ObjectIdentity=ObjectIdentity
begemotAtmNgGroup=_BegemotAtmNgGroup_ObjectIdentity((1,3,6,1,4,1,12325,1,101,1,4,1,1))
_BegemotAtmNgIfTable_Object=MibTable
begemotAtmNgIfTable=_BegemotAtmNgIfTable_Object((1,3,6,1,4,1,12325,1,101,1,4,1,1,1))
if mibBuilder.loadTexts:begemotAtmNgIfTable.setStatus(_A)
_BegemotAtmNgIfEntry_Object=MibTableRow
begemotAtmNgIfEntry=_BegemotAtmNgIfEntry_Object((1,3,6,1,4,1,12325,1,101,1,4,1,1,1,1))
if mibBuilder.loadTexts:begemotAtmNgIfEntry.setStatus(_A)
_BegemotAtmNgIfNodeId_Type=NgNodeIdOrZero
_BegemotAtmNgIfNodeId_Object=MibTableColumn
begemotAtmNgIfNodeId=_BegemotAtmNgIfNodeId_Object((1,3,6,1,4,1,12325,1,101,1,4,1,1,1,1,1),_BegemotAtmNgIfNodeId_Type())
begemotAtmNgIfNodeId.setMaxAccess('read-only')
if mibBuilder.loadTexts:begemotAtmNgIfNodeId.setStatus(_A)
begemotAtmIfEntry.registerAugmentions((_B,_C))
begemotAtmNgIfEntry.setIndexNames(*begemotAtmIfEntry.getIndexNames())
mibBuilder.exportSymbols(_B,**{'begemotAtmFreeBSDGroup':begemotAtmFreeBSDGroup,'begemotAtmNgGroup':begemotAtmNgGroup,'begemotAtmNgIfTable':begemotAtmNgIfTable,_C:begemotAtmNgIfEntry,'begemotAtmNgIfNodeId':begemotAtmNgIfNodeId})