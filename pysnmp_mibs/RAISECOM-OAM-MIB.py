_N='dot3OamPeerVendorOui'
_M='dot3OamPeerVendorInfo'
_L='dot3OamPeerMacAddress'
_K='OctetString'
_J='read-only'
_I='dot3OamEventLogType'
_H='dot3OamEventLogOui'
_G='dot3OamEventLogLocation'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-write'
_B='DOT3-OAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot3OamEventLogLocation,dot3OamEventLogOui,dot3OamEventLogType,dot3OamPeerMacAddress,dot3OamPeerVendorInfo,dot3OamPeerVendorOui=mibBuilder.importSymbols(_B,_G,_H,_I,_L,_M,_N)
ifIndex,=mibBuilder.importSymbols(_E,_F)
oam,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','oam')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
raisecomOamMIB=ModuleIdentity((1,3,6,1,4,1,8886,17,1,2))
if mibBuilder.loadTexts:raisecomOamMIB.setRevisions(('2006-09-05 00:00',))
_RaisecomOamObjects_ObjectIdentity=ObjectIdentity
raisecomOamObjects=_RaisecomOamObjects_ObjectIdentity((1,3,6,1,4,1,8886,17,1,2,1))
_RaisecomOamTrapTable_Object=MibTable
raisecomOamTrapTable=_RaisecomOamTrapTable_Object((1,3,6,1,4,1,8886,17,1,2,1,1))
if mibBuilder.loadTexts:raisecomOamTrapTable.setStatus(_A)
_RaisecomOamTrapEntry_Object=MibTableRow
raisecomOamTrapEntry=_RaisecomOamTrapEntry_Object((1,3,6,1,4,1,8886,17,1,2,1,1,1))
raisecomOamTrapEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomOamTrapEntry.setStatus(_A)
_RaisecomOamEventTrapEnable_Type=TruthValue
_RaisecomOamEventTrapEnable_Object=MibTableColumn
raisecomOamEventTrapEnable=_RaisecomOamEventTrapEnable_Object((1,3,6,1,4,1,8886,17,1,2,1,1,1,1),_RaisecomOamEventTrapEnable_Type())
raisecomOamEventTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOamEventTrapEnable.setStatus(_A)
_RaisecomOamPeerEventTrapEnable_Type=TruthValue
_RaisecomOamPeerEventTrapEnable_Object=MibTableColumn
raisecomOamPeerEventTrapEnable=_RaisecomOamPeerEventTrapEnable_Object((1,3,6,1,4,1,8886,17,1,2,1,1,1,2),_RaisecomOamPeerEventTrapEnable_Type())
raisecomOamPeerEventTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOamPeerEventTrapEnable.setStatus(_A)
_RaisecomOamDiscoveryTrapTotal_Type=Unsigned32
_RaisecomOamDiscoveryTrapTotal_Object=MibTableColumn
raisecomOamDiscoveryTrapTotal=_RaisecomOamDiscoveryTrapTotal_Object((1,3,6,1,4,1,8886,17,1,2,1,1,1,3),_RaisecomOamDiscoveryTrapTotal_Type())
raisecomOamDiscoveryTrapTotal.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomOamDiscoveryTrapTotal.setStatus(_A)
_RaisecomOamDiscoveryTrapTimestamp_Type=TimeStamp
_RaisecomOamDiscoveryTrapTimestamp_Object=MibTableColumn
raisecomOamDiscoveryTrapTimestamp=_RaisecomOamDiscoveryTrapTimestamp_Object((1,3,6,1,4,1,8886,17,1,2,1,1,1,4),_RaisecomOamDiscoveryTrapTimestamp_Type())
raisecomOamDiscoveryTrapTimestamp.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomOamDiscoveryTrapTimestamp.setStatus(_A)
_RaisecomOamLostTrapTotal_Type=Unsigned32
_RaisecomOamLostTrapTotal_Object=MibTableColumn
raisecomOamLostTrapTotal=_RaisecomOamLostTrapTotal_Object((1,3,6,1,4,1,8886,17,1,2,1,1,1,5),_RaisecomOamLostTrapTotal_Type())
raisecomOamLostTrapTotal.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomOamLostTrapTotal.setStatus(_A)
_RaisecomOamLostTrapTimestamp_Type=TimeStamp
_RaisecomOamLostTrapTimestamp_Object=MibTableColumn
raisecomOamLostTrapTimestamp=_RaisecomOamLostTrapTimestamp_Object((1,3,6,1,4,1,8886,17,1,2,1,1,1,6),_RaisecomOamLostTrapTimestamp_Type())
raisecomOamLostTrapTimestamp.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomOamLostTrapTimestamp.setStatus(_A)
_RaisecomOamRemoteMgtTable_Object=MibTable
raisecomOamRemoteMgtTable=_RaisecomOamRemoteMgtTable_Object((1,3,6,1,4,1,8886,17,1,2,1,2))
if mibBuilder.loadTexts:raisecomOamRemoteMgtTable.setStatus(_A)
_RaisecomOamRemoteMgtEntry_Object=MibTableRow
raisecomOamRemoteMgtEntry=_RaisecomOamRemoteMgtEntry_Object((1,3,6,1,4,1,8886,17,1,2,1,2,1))
raisecomOamRemoteMgtEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomOamRemoteMgtEntry.setStatus(_A)
class _RaisecomOamRemoteMgtBranch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,7)));namedValues=NamedValues(*(('object',3),('package',4),('attribute',7)))
_RaisecomOamRemoteMgtBranch_Type.__name__=_D
_RaisecomOamRemoteMgtBranch_Object=MibTableColumn
raisecomOamRemoteMgtBranch=_RaisecomOamRemoteMgtBranch_Object((1,3,6,1,4,1,8886,17,1,2,1,2,1,1),_RaisecomOamRemoteMgtBranch_Type())
raisecomOamRemoteMgtBranch.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOamRemoteMgtBranch.setStatus(_A)
class _RaisecomOamRemoteMgtLeaf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RaisecomOamRemoteMgtLeaf_Type.__name__=_D
_RaisecomOamRemoteMgtLeaf_Object=MibTableColumn
raisecomOamRemoteMgtLeaf=_RaisecomOamRemoteMgtLeaf_Object((1,3,6,1,4,1,8886,17,1,2,1,2,1,2),_RaisecomOamRemoteMgtLeaf_Type())
raisecomOamRemoteMgtLeaf.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOamRemoteMgtLeaf.setStatus(_A)
class _RaisecomOamRemoteMgtValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,512))
_RaisecomOamRemoteMgtValue_Type.__name__=_K
_RaisecomOamRemoteMgtValue_Object=MibTableColumn
raisecomOamRemoteMgtValue=_RaisecomOamRemoteMgtValue_Object((1,3,6,1,4,1,8886,17,1,2,1,2,1,3),_RaisecomOamRemoteMgtValue_Type())
raisecomOamRemoteMgtValue.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOamRemoteMgtValue.setStatus(_A)
class _RaisecomOamRemoteMgtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ok',0),('wait',1),('get',2)))
_RaisecomOamRemoteMgtStatus_Type.__name__=_D
_RaisecomOamRemoteMgtStatus_Object=MibTableColumn
raisecomOamRemoteMgtStatus=_RaisecomOamRemoteMgtStatus_Object((1,3,6,1,4,1,8886,17,1,2,1,2,1,4),_RaisecomOamRemoteMgtStatus_Type())
raisecomOamRemoteMgtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOamRemoteMgtStatus.setStatus(_A)
_RaisecomOamNotifications_ObjectIdentity=ObjectIdentity
raisecomOamNotifications=_RaisecomOamNotifications_ObjectIdentity((1,3,6,1,4,1,8886,17,1,2,2))
_RaisecomOamScalar_ObjectIdentity=ObjectIdentity
raisecomOamScalar=_RaisecomOamScalar_ObjectIdentity((1,3,6,1,4,1,8886,17,1,2,3))
class _RaisecomOamSendPeriod_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RaisecomOamSendPeriod_Type.__name__=_D
_RaisecomOamSendPeriod_Object=MibScalar
raisecomOamSendPeriod=_RaisecomOamSendPeriod_Object((1,3,6,1,4,1,8886,17,1,2,3,1),_RaisecomOamSendPeriod_Type())
raisecomOamSendPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOamSendPeriod.setStatus(_A)
class _RaisecomOamLinkTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RaisecomOamLinkTimeout_Type.__name__=_D
_RaisecomOamLinkTimeout_Object=MibScalar
raisecomOamLinkTimeout=_RaisecomOamLinkTimeout_Object((1,3,6,1,4,1,8886,17,1,2,3,2),_RaisecomOamLinkTimeout_Type())
raisecomOamLinkTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOamLinkTimeout.setStatus(_A)
raisecomOamDiscoveryTrap=NotificationType((1,3,6,1,4,1,8886,17,1,2,2,1))
raisecomOamDiscoveryTrap.setObjects(*((_E,_F),(_B,_L),(_B,_N),(_B,_M)))
if mibBuilder.loadTexts:raisecomOamDiscoveryTrap.setStatus(_A)
raisecomOamLostTrap=NotificationType((1,3,6,1,4,1,8886,17,1,2,2,2))
raisecomOamLostTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomOamLostTrap.setStatus(_A)
raisecomOamNormalTrap=NotificationType((1,3,6,1,4,1,8886,17,1,2,2,3))
raisecomOamNormalTrap.setObjects(*((_B,_H),(_B,_I),(_B,_G)))
if mibBuilder.loadTexts:raisecomOamNormalTrap.setStatus(_A)
raisecomOamDyingGaspNormalTrap=NotificationType((1,3,6,1,4,1,8886,17,1,2,2,4))
raisecomOamDyingGaspNormalTrap.setObjects(*((_B,_H),(_B,_I),(_B,_G)))
if mibBuilder.loadTexts:raisecomOamDyingGaspNormalTrap.setStatus(_A)
raisecomOamLinkFaultNormalTrap=NotificationType((1,3,6,1,4,1,8886,17,1,2,2,5))
raisecomOamLinkFaultNormalTrap.setObjects(*((_B,_H),(_B,_I),(_B,_G)))
if mibBuilder.loadTexts:raisecomOamLinkFaultNormalTrap.setStatus(_A)
mibBuilder.exportSymbols('RAISECOM-OAM-MIB',**{'raisecomOamMIB':raisecomOamMIB,'raisecomOamObjects':raisecomOamObjects,'raisecomOamTrapTable':raisecomOamTrapTable,'raisecomOamTrapEntry':raisecomOamTrapEntry,'raisecomOamEventTrapEnable':raisecomOamEventTrapEnable,'raisecomOamPeerEventTrapEnable':raisecomOamPeerEventTrapEnable,'raisecomOamDiscoveryTrapTotal':raisecomOamDiscoveryTrapTotal,'raisecomOamDiscoveryTrapTimestamp':raisecomOamDiscoveryTrapTimestamp,'raisecomOamLostTrapTotal':raisecomOamLostTrapTotal,'raisecomOamLostTrapTimestamp':raisecomOamLostTrapTimestamp,'raisecomOamRemoteMgtTable':raisecomOamRemoteMgtTable,'raisecomOamRemoteMgtEntry':raisecomOamRemoteMgtEntry,'raisecomOamRemoteMgtBranch':raisecomOamRemoteMgtBranch,'raisecomOamRemoteMgtLeaf':raisecomOamRemoteMgtLeaf,'raisecomOamRemoteMgtValue':raisecomOamRemoteMgtValue,'raisecomOamRemoteMgtStatus':raisecomOamRemoteMgtStatus,'raisecomOamNotifications':raisecomOamNotifications,'raisecomOamDiscoveryTrap':raisecomOamDiscoveryTrap,'raisecomOamLostTrap':raisecomOamLostTrap,'raisecomOamNormalTrap':raisecomOamNormalTrap,'raisecomOamDyingGaspNormalTrap':raisecomOamDyingGaspNormalTrap,'raisecomOamLinkFaultNormalTrap':raisecomOamLinkFaultNormalTrap,'raisecomOamScalar':raisecomOamScalar,'raisecomOamSendPeriod':raisecomOamSendPeriod,'raisecomOamLinkTimeout':raisecomOamLinkTimeout})