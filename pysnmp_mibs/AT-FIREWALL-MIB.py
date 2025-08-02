_G='firewallTrapMessage'
_F='nodeIpAddress'
_E='mandatory'
_D='Integer32'
_C='AT-FIREWALL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
firewall=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,77))
if mibBuilder.loadTexts:firewall.setRevisions(('2006-06-28 12:22',))
_FirewallTraps_ObjectIdentity=ObjectIdentity
firewallTraps=_FirewallTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,77,0))
_FirewallTrapMessage_Type=DisplayString
_FirewallTrapMessage_Object=MibScalar
firewallTrapMessage=_FirewallTrapMessage_Object((1,3,6,1,4,1,207,8,4,4,4,77,1),_FirewallTrapMessage_Type())
firewallTrapMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallTrapMessage.setStatus(_A)
_FirewallSessionsStatistics_ObjectIdentity=ObjectIdentity
firewallSessionsStatistics=_FirewallSessionsStatistics_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,77,2))
_TotalNumberOfSessions_Type=Gauge32
_TotalNumberOfSessions_Object=MibScalar
totalNumberOfSessions=_TotalNumberOfSessions_Object((1,3,6,1,4,1,207,8,4,4,4,77,2,1),_TotalNumberOfSessions_Type())
totalNumberOfSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:totalNumberOfSessions.setStatus(_E)
class _NumberOfSessionsPerNodeCountingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_NumberOfSessionsPerNodeCountingStatus_Type.__name__=_D
_NumberOfSessionsPerNodeCountingStatus_Object=MibScalar
numberOfSessionsPerNodeCountingStatus=_NumberOfSessionsPerNodeCountingStatus_Object((1,3,6,1,4,1,207,8,4,4,4,77,2,2),_NumberOfSessionsPerNodeCountingStatus_Type())
numberOfSessionsPerNodeCountingStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:numberOfSessionsPerNodeCountingStatus.setStatus(_E)
_NumberOfSessionsPerNodeTable_Object=MibTable
numberOfSessionsPerNodeTable=_NumberOfSessionsPerNodeTable_Object((1,3,6,1,4,1,207,8,4,4,4,77,2,3))
if mibBuilder.loadTexts:numberOfSessionsPerNodeTable.setStatus(_A)
_NumberOfSessionsPerNodeEntry_Object=MibTableRow
numberOfSessionsPerNodeEntry=_NumberOfSessionsPerNodeEntry_Object((1,3,6,1,4,1,207,8,4,4,4,77,2,3,1))
numberOfSessionsPerNodeEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:numberOfSessionsPerNodeEntry.setStatus(_A)
_NodeIpAddress_Type=IpAddress
_NodeIpAddress_Object=MibTableColumn
nodeIpAddress=_NodeIpAddress_Object((1,3,6,1,4,1,207,8,4,4,4,77,2,3,1,1),_NodeIpAddress_Type())
nodeIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeIpAddress.setStatus(_A)
_NumberOfSessionsPerNode_Type=Gauge32
_NumberOfSessionsPerNode_Object=MibTableColumn
numberOfSessionsPerNode=_NumberOfSessionsPerNode_Object((1,3,6,1,4,1,207,8,4,4,4,77,2,3,1,2),_NumberOfSessionsPerNode_Type())
numberOfSessionsPerNode.setMaxAccess(_B)
if mibBuilder.loadTexts:numberOfSessionsPerNode.setStatus(_A)
firewallTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,77,0,1))
firewallTrap.setObjects((_C,_G))
if mibBuilder.loadTexts:firewallTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'firewall':firewall,'firewallTraps':firewallTraps,'firewallTrap':firewallTrap,_G:firewallTrapMessage,'firewallSessionsStatistics':firewallSessionsStatistics,'totalNumberOfSessions':totalNumberOfSessions,'numberOfSessionsPerNodeCountingStatus':numberOfSessionsPerNodeCountingStatus,'numberOfSessionsPerNodeTable':numberOfSessionsPerNodeTable,'numberOfSessionsPerNodeEntry':numberOfSessionsPerNodeEntry,_F:nodeIpAddress,'numberOfSessionsPerNode':numberOfSessionsPerNode})