_P='rstpPortGroup'
_O='rstpBridgeGroup'
_N='dot1dStpPortAdminPathCost'
_M='dot1dStpPortOperPointToPoint'
_L='dot1dStpPortAdminPointToPoint'
_K='dot1dStpPortOperEdgePort'
_J='dot1dStpPortAdminEdgePort'
_I='dot1dStpPortProtocolMigration'
_H='dot1dStpTxHoldCount'
_G='dot1dStpVersion'
_F='dot1dStpExtPortEntry'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='RSTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStp,dot1dStpPortEntry=mibBuilder.importSymbols('BRIDGE-MIB','dot1dStp','dot1dStpPortEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rstpMIB=ModuleIdentity((1,3,6,1,2,1,134))
if mibBuilder.loadTexts:rstpMIB.setRevisions(('2005-12-07 00:00',))
class _Dot1dStpVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2)))
_Dot1dStpVersion_Type.__name__=_D
_Dot1dStpVersion_Object=MibScalar
dot1dStpVersion=_Dot1dStpVersion_Object((1,3,6,1,2,1,17,2,16),_Dot1dStpVersion_Type())
dot1dStpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dStpVersion.setStatus(_A)
class _Dot1dStpTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Dot1dStpTxHoldCount_Type.__name__=_D
_Dot1dStpTxHoldCount_Object=MibScalar
dot1dStpTxHoldCount=_Dot1dStpTxHoldCount_Object((1,3,6,1,2,1,17,2,17),_Dot1dStpTxHoldCount_Type())
dot1dStpTxHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dStpTxHoldCount.setStatus(_A)
_Dot1dStpExtPortTable_Object=MibTable
dot1dStpExtPortTable=_Dot1dStpExtPortTable_Object((1,3,6,1,2,1,17,2,19))
if mibBuilder.loadTexts:dot1dStpExtPortTable.setStatus(_A)
_Dot1dStpExtPortEntry_Object=MibTableRow
dot1dStpExtPortEntry=_Dot1dStpExtPortEntry_Object((1,3,6,1,2,1,17,2,19,1))
if mibBuilder.loadTexts:dot1dStpExtPortEntry.setStatus(_A)
_Dot1dStpPortProtocolMigration_Type=TruthValue
_Dot1dStpPortProtocolMigration_Object=MibTableColumn
dot1dStpPortProtocolMigration=_Dot1dStpPortProtocolMigration_Object((1,3,6,1,2,1,17,2,19,1,1),_Dot1dStpPortProtocolMigration_Type())
dot1dStpPortProtocolMigration.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dStpPortProtocolMigration.setStatus(_A)
_Dot1dStpPortAdminEdgePort_Type=TruthValue
_Dot1dStpPortAdminEdgePort_Object=MibTableColumn
dot1dStpPortAdminEdgePort=_Dot1dStpPortAdminEdgePort_Object((1,3,6,1,2,1,17,2,19,1,2),_Dot1dStpPortAdminEdgePort_Type())
dot1dStpPortAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dStpPortAdminEdgePort.setStatus(_A)
_Dot1dStpPortOperEdgePort_Type=TruthValue
_Dot1dStpPortOperEdgePort_Object=MibTableColumn
dot1dStpPortOperEdgePort=_Dot1dStpPortOperEdgePort_Object((1,3,6,1,2,1,17,2,19,1,3),_Dot1dStpPortOperEdgePort_Type())
dot1dStpPortOperEdgePort.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1dStpPortOperEdgePort.setStatus(_A)
class _Dot1dStpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_Dot1dStpPortAdminPointToPoint_Type.__name__=_D
_Dot1dStpPortAdminPointToPoint_Object=MibTableColumn
dot1dStpPortAdminPointToPoint=_Dot1dStpPortAdminPointToPoint_Object((1,3,6,1,2,1,17,2,19,1,4),_Dot1dStpPortAdminPointToPoint_Type())
dot1dStpPortAdminPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dStpPortAdminPointToPoint.setStatus(_A)
_Dot1dStpPortOperPointToPoint_Type=TruthValue
_Dot1dStpPortOperPointToPoint_Object=MibTableColumn
dot1dStpPortOperPointToPoint=_Dot1dStpPortOperPointToPoint_Object((1,3,6,1,2,1,17,2,19,1,5),_Dot1dStpPortOperPointToPoint_Type())
dot1dStpPortOperPointToPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1dStpPortOperPointToPoint.setStatus(_A)
class _Dot1dStpPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_Dot1dStpPortAdminPathCost_Type.__name__=_D
_Dot1dStpPortAdminPathCost_Object=MibTableColumn
dot1dStpPortAdminPathCost=_Dot1dStpPortAdminPathCost_Object((1,3,6,1,2,1,17,2,19,1,6),_Dot1dStpPortAdminPathCost_Type())
dot1dStpPortAdminPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dStpPortAdminPathCost.setStatus(_A)
_RstpNotifications_ObjectIdentity=ObjectIdentity
rstpNotifications=_RstpNotifications_ObjectIdentity((1,3,6,1,2,1,134,0))
_RstpObjects_ObjectIdentity=ObjectIdentity
rstpObjects=_RstpObjects_ObjectIdentity((1,3,6,1,2,1,134,1))
_RstpConformance_ObjectIdentity=ObjectIdentity
rstpConformance=_RstpConformance_ObjectIdentity((1,3,6,1,2,1,134,2))
_RstpGroups_ObjectIdentity=ObjectIdentity
rstpGroups=_RstpGroups_ObjectIdentity((1,3,6,1,2,1,134,2,1))
_RstpCompliances_ObjectIdentity=ObjectIdentity
rstpCompliances=_RstpCompliances_ObjectIdentity((1,3,6,1,2,1,134,2,2))
dot1dStpPortEntry.registerAugmentions((_B,_F))
dot1dStpExtPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
rstpBridgeGroup=ObjectGroup((1,3,6,1,2,1,134,2,1,1))
rstpBridgeGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:rstpBridgeGroup.setStatus(_A)
rstpPortGroup=ObjectGroup((1,3,6,1,2,1,134,2,1,2))
rstpPortGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:rstpPortGroup.setStatus(_A)
rstpCompliance=ModuleCompliance((1,3,6,1,2,1,134,2,2,1))
rstpCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:rstpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:dot1dStpVersion,_H:dot1dStpTxHoldCount,'dot1dStpExtPortTable':dot1dStpExtPortTable,_F:dot1dStpExtPortEntry,_I:dot1dStpPortProtocolMigration,_J:dot1dStpPortAdminEdgePort,_K:dot1dStpPortOperEdgePort,_L:dot1dStpPortAdminPointToPoint,_M:dot1dStpPortOperPointToPoint,_N:dot1dStpPortAdminPathCost,'rstpMIB':rstpMIB,'rstpNotifications':rstpNotifications,'rstpObjects':rstpObjects,'rstpConformance':rstpConformance,'rstpGroups':rstpGroups,_O:rstpBridgeGroup,_P:rstpPortGroup,'rstpCompliances':rstpCompliances,'rstpCompliance':rstpCompliance})