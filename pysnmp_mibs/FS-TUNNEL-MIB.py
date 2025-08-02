_D='read-only'
_C='fsTunnelIp'
_B='FS-TUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsTunnelMib=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,114))
if mibBuilder.loadTexts:fsTunnelMib.setRevisions(('2012-06-20 00:00',))
_FsTunnelObjects_ObjectIdentity=ObjectIdentity
fsTunnelObjects=_FsTunnelObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,114,1))
_FsTunnelTable_Object=MibTable
fsTunnelTable=_FsTunnelTable_Object((1,3,6,1,4,1,52642,1,1,10,2,114,1,1))
if mibBuilder.loadTexts:fsTunnelTable.setStatus(_A)
_FsTunnelEntry_Object=MibTableRow
fsTunnelEntry=_FsTunnelEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,114,1,1,1))
fsTunnelEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:fsTunnelEntry.setStatus(_A)
_FsTunnelIp_Type=IpAddress
_FsTunnelIp_Object=MibTableColumn
fsTunnelIp=_FsTunnelIp_Object((1,3,6,1,4,1,52642,1,1,10,2,114,1,1,1,1),_FsTunnelIp_Type())
fsTunnelIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTunnelIp.setStatus(_A)
_FsTunnelOutIfindex_Type=Integer32
_FsTunnelOutIfindex_Object=MibTableColumn
fsTunnelOutIfindex=_FsTunnelOutIfindex_Object((1,3,6,1,4,1,52642,1,1,10,2,114,1,1,1,2),_FsTunnelOutIfindex_Type())
fsTunnelOutIfindex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTunnelOutIfindex.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsTunnelMib':fsTunnelMib,'fsTunnelObjects':fsTunnelObjects,'fsTunnelTable':fsTunnelTable,'fsTunnelEntry':fsTunnelEntry,_C:fsTunnelIp,'fsTunnelOutIfindex':fsTunnelOutIfindex})