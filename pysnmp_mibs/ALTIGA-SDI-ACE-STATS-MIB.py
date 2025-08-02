_Q='altigaACEServerGroup'
_P='alACEServerBadPinSent'
_O='alACEServerBadCodeSent'
_N='alACEServerAuthFailures'
_M='alACEServerAuthSuccesses'
_L='alACEServerGroupId'
_K='alACEServerTimeout'
_J='alACEServerRetries'
_I='alACEServerPort'
_H='alACEServerAddress'
_G='alACEServerPriority'
_F='alACEServerIndex'
_E='alACEPrimaryIndex'
_D='Integer32'
_C='read-only'
_B='ALTIGA-SDI-ACE-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alACEServerMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alACEServerMibModule')
alACEServerGroup,alACEServerStats=mibBuilder.importSymbols('ALTIGA-MIB','alACEServerGroup','alACEServerStats')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaACEStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,50,1))
if mibBuilder.loadTexts:altigaACEStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaACEStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaACEStatsMibConformance=_AltigaACEStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,50,1,1))
_AltigaACEStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaACEStatsMibCompliances=_AltigaACEStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,50,1,1,1))
_AlCfgACEGlobal_ObjectIdentity=ObjectIdentity
alCfgACEGlobal=_AlCfgACEGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,45,1))
_AlACEServerTable_Object=MibTable
alACEServerTable=_AlACEServerTable_Object((1,3,6,1,4,1,3076,2,1,2,45,2))
if mibBuilder.loadTexts:alACEServerTable.setStatus(_A)
_AlACEServerEntry_Object=MibTableRow
alACEServerEntry=_AlACEServerEntry_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1))
alACEServerEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:alACEServerEntry.setStatus(_A)
_AlACEPrimaryIndex_Type=Integer32
_AlACEPrimaryIndex_Object=MibTableColumn
alACEPrimaryIndex=_AlACEPrimaryIndex_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,1),_AlACEPrimaryIndex_Type())
alACEPrimaryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEPrimaryIndex.setStatus(_A)
class _AlACEServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AlACEServerIndex_Type.__name__=_D
_AlACEServerIndex_Object=MibTableColumn
alACEServerIndex=_AlACEServerIndex_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,2),_AlACEServerIndex_Type())
alACEServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerIndex.setStatus(_A)
class _AlACEServerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AlACEServerPriority_Type.__name__=_D
_AlACEServerPriority_Object=MibTableColumn
alACEServerPriority=_AlACEServerPriority_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,3),_AlACEServerPriority_Type())
alACEServerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerPriority.setStatus(_A)
_AlACEServerAddress_Type=IpAddress
_AlACEServerAddress_Object=MibTableColumn
alACEServerAddress=_AlACEServerAddress_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,4),_AlACEServerAddress_Type())
alACEServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerAddress.setStatus(_A)
class _AlACEServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlACEServerPort_Type.__name__=_D
_AlACEServerPort_Object=MibTableColumn
alACEServerPort=_AlACEServerPort_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,5),_AlACEServerPort_Type())
alACEServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerPort.setStatus(_A)
_AlACEServerRetries_Type=Counter32
_AlACEServerRetries_Object=MibTableColumn
alACEServerRetries=_AlACEServerRetries_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,6),_AlACEServerRetries_Type())
alACEServerRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerRetries.setStatus(_A)
_AlACEServerTimeout_Type=Counter32
_AlACEServerTimeout_Object=MibTableColumn
alACEServerTimeout=_AlACEServerTimeout_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,7),_AlACEServerTimeout_Type())
alACEServerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerTimeout.setStatus(_A)
_AlACEServerGroupId_Type=Gauge32
_AlACEServerGroupId_Object=MibTableColumn
alACEServerGroupId=_AlACEServerGroupId_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,8),_AlACEServerGroupId_Type())
alACEServerGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerGroupId.setStatus(_A)
_AlACEServerAuthSuccesses_Type=Counter32
_AlACEServerAuthSuccesses_Object=MibTableColumn
alACEServerAuthSuccesses=_AlACEServerAuthSuccesses_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,9),_AlACEServerAuthSuccesses_Type())
alACEServerAuthSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerAuthSuccesses.setStatus(_A)
_AlACEServerAuthFailures_Type=Counter32
_AlACEServerAuthFailures_Object=MibTableColumn
alACEServerAuthFailures=_AlACEServerAuthFailures_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,10),_AlACEServerAuthFailures_Type())
alACEServerAuthFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerAuthFailures.setStatus(_A)
_AlACEServerBadCodeSent_Type=Counter32
_AlACEServerBadCodeSent_Object=MibTableColumn
alACEServerBadCodeSent=_AlACEServerBadCodeSent_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,11),_AlACEServerBadCodeSent_Type())
alACEServerBadCodeSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerBadCodeSent.setStatus(_A)
_AlACEServerBadPinSent_Type=Counter32
_AlACEServerBadPinSent_Object=MibTableColumn
alACEServerBadPinSent=_AlACEServerBadPinSent_Object((1,3,6,1,4,1,3076,2,1,2,45,2,1,12),_AlACEServerBadPinSent_Type())
alACEServerBadPinSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alACEServerBadPinSent.setStatus(_A)
altigaACEServerGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,45,1))
altigaACEServerGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:altigaACEServerGroup.setStatus(_A)
altigaACEStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,50,1,1,1,1))
altigaACEStatsMibCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:altigaACEStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaACEStatsMibModule':altigaACEStatsMibModule,'altigaACEStatsMibConformance':altigaACEStatsMibConformance,'altigaACEStatsMibCompliances':altigaACEStatsMibCompliances,'altigaACEStatsMibCompliance':altigaACEStatsMibCompliance,_Q:altigaACEServerGroup,'alCfgACEGlobal':alCfgACEGlobal,'alACEServerTable':alACEServerTable,'alACEServerEntry':alACEServerEntry,_E:alACEPrimaryIndex,_F:alACEServerIndex,_G:alACEServerPriority,_H:alACEServerAddress,_I:alACEServerPort,_J:alACEServerRetries,_K:alACEServerTimeout,_L:alACEServerGroupId,_M:alACEServerAuthSuccesses,_N:alACEServerAuthFailures,_O:alACEServerBadCodeSent,_P:alACEServerBadPinSent})