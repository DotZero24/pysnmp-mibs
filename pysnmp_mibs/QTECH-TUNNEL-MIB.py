_D='read-only'
_C='qtechTunnelIp'
_B='QTECH-TUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechTunnelMib=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,114))
if mibBuilder.loadTexts:qtechTunnelMib.setRevisions(('2012-06-20 00:00',))
_QtechTunnelObjects_ObjectIdentity=ObjectIdentity
qtechTunnelObjects=_QtechTunnelObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,114,1))
_QtechTunnelTable_Object=MibTable
qtechTunnelTable=_QtechTunnelTable_Object((1,3,6,1,4,1,27514,1,1,10,2,114,1,1))
if mibBuilder.loadTexts:qtechTunnelTable.setStatus(_A)
_QtechTunnelEntry_Object=MibTableRow
qtechTunnelEntry=_QtechTunnelEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,114,1,1,1))
qtechTunnelEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:qtechTunnelEntry.setStatus(_A)
_QtechTunnelIp_Type=IpAddress
_QtechTunnelIp_Object=MibTableColumn
qtechTunnelIp=_QtechTunnelIp_Object((1,3,6,1,4,1,27514,1,1,10,2,114,1,1,1,1),_QtechTunnelIp_Type())
qtechTunnelIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTunnelIp.setStatus(_A)
_QtechTunnelOutIfindex_Type=Integer32
_QtechTunnelOutIfindex_Object=MibTableColumn
qtechTunnelOutIfindex=_QtechTunnelOutIfindex_Object((1,3,6,1,4,1,27514,1,1,10,2,114,1,1,1,2),_QtechTunnelOutIfindex_Type())
qtechTunnelOutIfindex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTunnelOutIfindex.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechTunnelMib':qtechTunnelMib,'qtechTunnelObjects':qtechTunnelObjects,'qtechTunnelTable':qtechTunnelTable,'qtechTunnelEntry':qtechTunnelEntry,_C:qtechTunnelIp,'qtechTunnelOutIfindex':qtechTunnelOutIfindex})