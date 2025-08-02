_F='mitelBackupWANServerIPAddr'
_E='MITEL-WANBACKUP-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mitelIpGrpBackupWANGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,1,6))
if mibBuilder.loadTexts:mitelIpGrpBackupWANGroup.setRevisions(('2003-03-24 11:03','1999-03-01 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelRouterIpGroup_ObjectIdentity=ObjectIdentity
mitelRouterIpGroup=_MitelRouterIpGroup_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,1))
_MitelBackupWANDestIndex_Type=Integer32
_MitelBackupWANDestIndex_Object=MibScalar
mitelBackupWANDestIndex=_MitelBackupWANDestIndex_Object((1,3,6,1,4,1,1027,4,8,1,1,6,1),_MitelBackupWANDestIndex_Type())
mitelBackupWANDestIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mitelBackupWANDestIndex.setStatus(_A)
class _MitelBackupWANEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_MitelBackupWANEnable_Type.__name__=_B
_MitelBackupWANEnable_Object=MibScalar
mitelBackupWANEnable=_MitelBackupWANEnable_Object((1,3,6,1,4,1,1027,4,8,1,1,6,2),_MitelBackupWANEnable_Type())
mitelBackupWANEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBackupWANEnable.setStatus(_A)
class _MitelBackupWANPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_MitelBackupWANPollFreq_Type.__name__=_B
_MitelBackupWANPollFreq_Object=MibScalar
mitelBackupWANPollFreq=_MitelBackupWANPollFreq_Object((1,3,6,1,4,1,1027,4,8,1,1,6,3),_MitelBackupWANPollFreq_Type())
mitelBackupWANPollFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBackupWANPollFreq.setStatus(_A)
class _MitelBackupWANLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('down',2)))
_MitelBackupWANLinkStatus_Type.__name__=_B
_MitelBackupWANLinkStatus_Object=MibScalar
mitelBackupWANLinkStatus=_MitelBackupWANLinkStatus_Object((1,3,6,1,4,1,1027,4,8,1,1,6,4),_MitelBackupWANLinkStatus_Type())
mitelBackupWANLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mitelBackupWANLinkStatus.setStatus(_A)
_MitelBackupWANServerTable_Object=MibTable
mitelBackupWANServerTable=_MitelBackupWANServerTable_Object((1,3,6,1,4,1,1027,4,8,1,1,6,5))
if mibBuilder.loadTexts:mitelBackupWANServerTable.setStatus(_A)
_MitelBackupWANServerEntry_Object=MibTableRow
mitelBackupWANServerEntry=_MitelBackupWANServerEntry_Object((1,3,6,1,4,1,1027,4,8,1,1,6,5,1))
mitelBackupWANServerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mitelBackupWANServerEntry.setStatus(_A)
_MitelBackupWANServerIPAddr_Type=IpAddress
_MitelBackupWANServerIPAddr_Object=MibTableColumn
mitelBackupWANServerIPAddr=_MitelBackupWANServerIPAddr_Object((1,3,6,1,4,1,1027,4,8,1,1,6,5,1,1),_MitelBackupWANServerIPAddr_Type())
mitelBackupWANServerIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBackupWANServerIPAddr.setStatus(_A)
_MitelBackupWANServerSubnetAddr_Type=IpAddress
_MitelBackupWANServerSubnetAddr_Object=MibTableColumn
mitelBackupWANServerSubnetAddr=_MitelBackupWANServerSubnetAddr_Object((1,3,6,1,4,1,1027,4,8,1,1,6,5,1,2),_MitelBackupWANServerSubnetAddr_Type())
mitelBackupWANServerSubnetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBackupWANServerSubnetAddr.setStatus(_A)
class _MitelBackupWANServerPrimary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_MitelBackupWANServerPrimary_Type.__name__=_B
_MitelBackupWANServerPrimary_Object=MibTableColumn
mitelBackupWANServerPrimary=_MitelBackupWANServerPrimary_Object((1,3,6,1,4,1,1027,4,8,1,1,6,5,1,3),_MitelBackupWANServerPrimary_Type())
mitelBackupWANServerPrimary.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBackupWANServerPrimary.setStatus(_A)
_MitelBackupWANServerStatus_Type=RowStatus
_MitelBackupWANServerStatus_Object=MibTableColumn
mitelBackupWANServerStatus=_MitelBackupWANServerStatus_Object((1,3,6,1,4,1,1027,4,8,1,1,6,5,1,4),_MitelBackupWANServerStatus_Type())
mitelBackupWANServerStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mitelBackupWANServerStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterIpGroup':mitelRouterIpGroup,'mitelIpGrpBackupWANGroup':mitelIpGrpBackupWANGroup,'mitelBackupWANDestIndex':mitelBackupWANDestIndex,'mitelBackupWANEnable':mitelBackupWANEnable,'mitelBackupWANPollFreq':mitelBackupWANPollFreq,'mitelBackupWANLinkStatus':mitelBackupWANLinkStatus,'mitelBackupWANServerTable':mitelBackupWANServerTable,'mitelBackupWANServerEntry':mitelBackupWANServerEntry,_F:mitelBackupWANServerIPAddr,'mitelBackupWANServerSubnetAddr':mitelBackupWANServerSubnetAddr,'mitelBackupWANServerPrimary':mitelBackupWANServerPrimary,'mitelBackupWANServerStatus':mitelBackupWANServerStatus})