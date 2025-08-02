_x='dsIntEntURL'
_w='dsIntEntSuccesses'
_v='dsIntEntFailures'
_u='dsIntEntFailuresSinceLastSuccess'
_t='dsIntEntTimeOfLastSuccess'
_s='dsIntEntTimeOfLastAttempt'
_r='dsIntEntTimeOfCreation'
_q='dsIntEntDirectoryName'
_p='dsApplIfOutBytes'
_o='dsApplIfInBytes'
_n='dsApplIfReplicationUpdatesOut'
_m='dsApplIfReplicationUpdatesIn'
_l='dsApplIfErrors'
_k='dsApplIfSecurityErrors'
_j='dsApplIfChainings'
_i='dsApplIfReferrals'
_h='dsApplIfWholeSubtreeSearchOps'
_g='dsApplIfOneLevelSearchOps'
_f='dsApplIfSearchOps'
_e='dsApplIfListOps'
_d='dsApplIfModifyRDNOps'
_c='dsApplIfModifyEntryOps'
_b='dsApplIfRemoveEntryOps'
_a='dsApplIfAddEntryOps'
_Z='dsApplIfCompareOps'
_Y='dsApplIfReadOps'
_X='dsApplIfInOps'
_W='dsApplIfBindSecurityErrors'
_V='dsApplIfStrongAuthBinds'
_U='dsApplIfSimpleAuthBinds'
_T='dsApplIfUnauthBinds'
_S='dsApplIfProtocol'
_R='dsSlaveHits'
_Q='dsCacheHits'
_P='dsCacheEntries'
_O='dsCopyEntries'
_N='dsMasterEntries'
_M='dsServerDescription'
_L='dsServerType'
_K='dsIntEntIndex'
_J='dsIntGroup'
_I='dsOpsGroup'
_H='Integer32'
_G='dsApplIfProtocolIndex'
_F='applIndex'
_E='NETWORK-SERVICES-MIB'
_D='dsEntryGroup'
_C='read-only'
_B='DIRECTORY-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DistinguishedName,URLString,applIndex=mibBuilder.importSymbols(_E,'DistinguishedName','URLString',_F)
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
dsMIB=ModuleIdentity((1,3,6,1,2,1,66))
if mibBuilder.loadTexts:dsMIB.setRevisions(('1999-06-07 00:00','1993-11-25 00:00'))
_DsTable_Object=MibTable
dsTable=_DsTable_Object((1,3,6,1,2,1,66,1))
if mibBuilder.loadTexts:dsTable.setStatus(_A)
_DsTableEntry_Object=MibTableRow
dsTableEntry=_DsTableEntry_Object((1,3,6,1,2,1,66,1,1))
dsTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dsTableEntry.setStatus(_A)
class _DsServerType_Type(Bits):namedValues=NamedValues(*(('frontEndDirectoryServer',0),('backEndDirectoryServer',1)))
_DsServerType_Type.__name__='Bits'
_DsServerType_Object=MibTableColumn
dsServerType=_DsServerType_Object((1,3,6,1,2,1,66,1,1,1),_DsServerType_Type())
dsServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:dsServerType.setStatus(_A)
_DsServerDescription_Type=DisplayString
_DsServerDescription_Object=MibTableColumn
dsServerDescription=_DsServerDescription_Object((1,3,6,1,2,1,66,1,1,2),_DsServerDescription_Type())
dsServerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:dsServerDescription.setStatus(_A)
_DsMasterEntries_Type=Gauge32
_DsMasterEntries_Object=MibTableColumn
dsMasterEntries=_DsMasterEntries_Object((1,3,6,1,2,1,66,1,1,3),_DsMasterEntries_Type())
dsMasterEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:dsMasterEntries.setStatus(_A)
_DsCopyEntries_Type=Gauge32
_DsCopyEntries_Object=MibTableColumn
dsCopyEntries=_DsCopyEntries_Object((1,3,6,1,2,1,66,1,1,4),_DsCopyEntries_Type())
dsCopyEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:dsCopyEntries.setStatus(_A)
_DsCacheEntries_Type=Gauge32
_DsCacheEntries_Object=MibTableColumn
dsCacheEntries=_DsCacheEntries_Object((1,3,6,1,2,1,66,1,1,5),_DsCacheEntries_Type())
dsCacheEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:dsCacheEntries.setStatus(_A)
_DsCacheHits_Type=Counter32
_DsCacheHits_Object=MibTableColumn
dsCacheHits=_DsCacheHits_Object((1,3,6,1,2,1,66,1,1,6),_DsCacheHits_Type())
dsCacheHits.setMaxAccess(_C)
if mibBuilder.loadTexts:dsCacheHits.setStatus(_A)
_DsSlaveHits_Type=Counter32
_DsSlaveHits_Object=MibTableColumn
dsSlaveHits=_DsSlaveHits_Object((1,3,6,1,2,1,66,1,1,7),_DsSlaveHits_Type())
dsSlaveHits.setMaxAccess(_C)
if mibBuilder.loadTexts:dsSlaveHits.setStatus(_A)
_DsApplIfOpsTable_Object=MibTable
dsApplIfOpsTable=_DsApplIfOpsTable_Object((1,3,6,1,2,1,66,2))
if mibBuilder.loadTexts:dsApplIfOpsTable.setStatus(_A)
_DsApplIfOpsEntry_Object=MibTableRow
dsApplIfOpsEntry=_DsApplIfOpsEntry_Object((1,3,6,1,2,1,66,2,1))
dsApplIfOpsEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:dsApplIfOpsEntry.setStatus(_A)
class _DsApplIfProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DsApplIfProtocolIndex_Type.__name__=_H
_DsApplIfProtocolIndex_Object=MibTableColumn
dsApplIfProtocolIndex=_DsApplIfProtocolIndex_Object((1,3,6,1,2,1,66,2,1,1),_DsApplIfProtocolIndex_Type())
dsApplIfProtocolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfProtocolIndex.setStatus(_A)
_DsApplIfProtocol_Type=ObjectIdentifier
_DsApplIfProtocol_Object=MibTableColumn
dsApplIfProtocol=_DsApplIfProtocol_Object((1,3,6,1,2,1,66,2,1,2),_DsApplIfProtocol_Type())
dsApplIfProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfProtocol.setStatus(_A)
_DsApplIfUnauthBinds_Type=Counter32
_DsApplIfUnauthBinds_Object=MibTableColumn
dsApplIfUnauthBinds=_DsApplIfUnauthBinds_Object((1,3,6,1,2,1,66,2,1,3),_DsApplIfUnauthBinds_Type())
dsApplIfUnauthBinds.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfUnauthBinds.setStatus(_A)
_DsApplIfSimpleAuthBinds_Type=Counter32
_DsApplIfSimpleAuthBinds_Object=MibTableColumn
dsApplIfSimpleAuthBinds=_DsApplIfSimpleAuthBinds_Object((1,3,6,1,2,1,66,2,1,4),_DsApplIfSimpleAuthBinds_Type())
dsApplIfSimpleAuthBinds.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfSimpleAuthBinds.setStatus(_A)
_DsApplIfStrongAuthBinds_Type=Counter32
_DsApplIfStrongAuthBinds_Object=MibTableColumn
dsApplIfStrongAuthBinds=_DsApplIfStrongAuthBinds_Object((1,3,6,1,2,1,66,2,1,5),_DsApplIfStrongAuthBinds_Type())
dsApplIfStrongAuthBinds.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfStrongAuthBinds.setStatus(_A)
_DsApplIfBindSecurityErrors_Type=Counter32
_DsApplIfBindSecurityErrors_Object=MibTableColumn
dsApplIfBindSecurityErrors=_DsApplIfBindSecurityErrors_Object((1,3,6,1,2,1,66,2,1,6),_DsApplIfBindSecurityErrors_Type())
dsApplIfBindSecurityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfBindSecurityErrors.setStatus(_A)
_DsApplIfInOps_Type=Counter32
_DsApplIfInOps_Object=MibTableColumn
dsApplIfInOps=_DsApplIfInOps_Object((1,3,6,1,2,1,66,2,1,7),_DsApplIfInOps_Type())
dsApplIfInOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfInOps.setStatus(_A)
_DsApplIfReadOps_Type=Counter32
_DsApplIfReadOps_Object=MibTableColumn
dsApplIfReadOps=_DsApplIfReadOps_Object((1,3,6,1,2,1,66,2,1,8),_DsApplIfReadOps_Type())
dsApplIfReadOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfReadOps.setStatus(_A)
_DsApplIfCompareOps_Type=Counter32
_DsApplIfCompareOps_Object=MibTableColumn
dsApplIfCompareOps=_DsApplIfCompareOps_Object((1,3,6,1,2,1,66,2,1,9),_DsApplIfCompareOps_Type())
dsApplIfCompareOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfCompareOps.setStatus(_A)
_DsApplIfAddEntryOps_Type=Counter32
_DsApplIfAddEntryOps_Object=MibTableColumn
dsApplIfAddEntryOps=_DsApplIfAddEntryOps_Object((1,3,6,1,2,1,66,2,1,10),_DsApplIfAddEntryOps_Type())
dsApplIfAddEntryOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfAddEntryOps.setStatus(_A)
_DsApplIfRemoveEntryOps_Type=Counter32
_DsApplIfRemoveEntryOps_Object=MibTableColumn
dsApplIfRemoveEntryOps=_DsApplIfRemoveEntryOps_Object((1,3,6,1,2,1,66,2,1,11),_DsApplIfRemoveEntryOps_Type())
dsApplIfRemoveEntryOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfRemoveEntryOps.setStatus(_A)
_DsApplIfModifyEntryOps_Type=Counter32
_DsApplIfModifyEntryOps_Object=MibTableColumn
dsApplIfModifyEntryOps=_DsApplIfModifyEntryOps_Object((1,3,6,1,2,1,66,2,1,12),_DsApplIfModifyEntryOps_Type())
dsApplIfModifyEntryOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfModifyEntryOps.setStatus(_A)
_DsApplIfModifyRDNOps_Type=Counter32
_DsApplIfModifyRDNOps_Object=MibTableColumn
dsApplIfModifyRDNOps=_DsApplIfModifyRDNOps_Object((1,3,6,1,2,1,66,2,1,13),_DsApplIfModifyRDNOps_Type())
dsApplIfModifyRDNOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfModifyRDNOps.setStatus(_A)
_DsApplIfListOps_Type=Counter32
_DsApplIfListOps_Object=MibTableColumn
dsApplIfListOps=_DsApplIfListOps_Object((1,3,6,1,2,1,66,2,1,14),_DsApplIfListOps_Type())
dsApplIfListOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfListOps.setStatus(_A)
_DsApplIfSearchOps_Type=Counter32
_DsApplIfSearchOps_Object=MibTableColumn
dsApplIfSearchOps=_DsApplIfSearchOps_Object((1,3,6,1,2,1,66,2,1,15),_DsApplIfSearchOps_Type())
dsApplIfSearchOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfSearchOps.setStatus(_A)
_DsApplIfOneLevelSearchOps_Type=Counter32
_DsApplIfOneLevelSearchOps_Object=MibTableColumn
dsApplIfOneLevelSearchOps=_DsApplIfOneLevelSearchOps_Object((1,3,6,1,2,1,66,2,1,16),_DsApplIfOneLevelSearchOps_Type())
dsApplIfOneLevelSearchOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfOneLevelSearchOps.setStatus(_A)
_DsApplIfWholeSubtreeSearchOps_Type=Counter32
_DsApplIfWholeSubtreeSearchOps_Object=MibTableColumn
dsApplIfWholeSubtreeSearchOps=_DsApplIfWholeSubtreeSearchOps_Object((1,3,6,1,2,1,66,2,1,17),_DsApplIfWholeSubtreeSearchOps_Type())
dsApplIfWholeSubtreeSearchOps.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfWholeSubtreeSearchOps.setStatus(_A)
_DsApplIfReferrals_Type=Counter32
_DsApplIfReferrals_Object=MibTableColumn
dsApplIfReferrals=_DsApplIfReferrals_Object((1,3,6,1,2,1,66,2,1,18),_DsApplIfReferrals_Type())
dsApplIfReferrals.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfReferrals.setStatus(_A)
_DsApplIfChainings_Type=Counter32
_DsApplIfChainings_Object=MibTableColumn
dsApplIfChainings=_DsApplIfChainings_Object((1,3,6,1,2,1,66,2,1,19),_DsApplIfChainings_Type())
dsApplIfChainings.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfChainings.setStatus(_A)
_DsApplIfSecurityErrors_Type=Counter32
_DsApplIfSecurityErrors_Object=MibTableColumn
dsApplIfSecurityErrors=_DsApplIfSecurityErrors_Object((1,3,6,1,2,1,66,2,1,20),_DsApplIfSecurityErrors_Type())
dsApplIfSecurityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfSecurityErrors.setStatus(_A)
_DsApplIfErrors_Type=Counter32
_DsApplIfErrors_Object=MibTableColumn
dsApplIfErrors=_DsApplIfErrors_Object((1,3,6,1,2,1,66,2,1,21),_DsApplIfErrors_Type())
dsApplIfErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfErrors.setStatus(_A)
_DsApplIfReplicationUpdatesIn_Type=Counter32
_DsApplIfReplicationUpdatesIn_Object=MibTableColumn
dsApplIfReplicationUpdatesIn=_DsApplIfReplicationUpdatesIn_Object((1,3,6,1,2,1,66,2,1,22),_DsApplIfReplicationUpdatesIn_Type())
dsApplIfReplicationUpdatesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfReplicationUpdatesIn.setStatus(_A)
_DsApplIfReplicationUpdatesOut_Type=Counter32
_DsApplIfReplicationUpdatesOut_Object=MibTableColumn
dsApplIfReplicationUpdatesOut=_DsApplIfReplicationUpdatesOut_Object((1,3,6,1,2,1,66,2,1,23),_DsApplIfReplicationUpdatesOut_Type())
dsApplIfReplicationUpdatesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfReplicationUpdatesOut.setStatus(_A)
_DsApplIfInBytes_Type=Counter32
_DsApplIfInBytes_Object=MibTableColumn
dsApplIfInBytes=_DsApplIfInBytes_Object((1,3,6,1,2,1,66,2,1,24),_DsApplIfInBytes_Type())
dsApplIfInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfInBytes.setStatus(_A)
_DsApplIfOutBytes_Type=Counter32
_DsApplIfOutBytes_Object=MibTableColumn
dsApplIfOutBytes=_DsApplIfOutBytes_Object((1,3,6,1,2,1,66,2,1,25),_DsApplIfOutBytes_Type())
dsApplIfOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:dsApplIfOutBytes.setStatus(_A)
_DsIntTable_Object=MibTable
dsIntTable=_DsIntTable_Object((1,3,6,1,2,1,66,3))
if mibBuilder.loadTexts:dsIntTable.setStatus(_A)
_DsIntEntry_Object=MibTableRow
dsIntEntry=_DsIntEntry_Object((1,3,6,1,2,1,66,3,1))
dsIntEntry.setIndexNames((0,_E,_F),(0,_B,_K),(0,_B,_G))
if mibBuilder.loadTexts:dsIntEntry.setStatus(_A)
class _DsIntEntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DsIntEntIndex_Type.__name__=_H
_DsIntEntIndex_Object=MibTableColumn
dsIntEntIndex=_DsIntEntIndex_Object((1,3,6,1,2,1,66,3,1,1),_DsIntEntIndex_Type())
dsIntEntIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dsIntEntIndex.setStatus(_A)
_DsIntEntDirectoryName_Type=DistinguishedName
_DsIntEntDirectoryName_Object=MibTableColumn
dsIntEntDirectoryName=_DsIntEntDirectoryName_Object((1,3,6,1,2,1,66,3,1,2),_DsIntEntDirectoryName_Type())
dsIntEntDirectoryName.setMaxAccess(_C)
if mibBuilder.loadTexts:dsIntEntDirectoryName.setStatus(_A)
_DsIntEntTimeOfCreation_Type=TimeStamp
_DsIntEntTimeOfCreation_Object=MibTableColumn
dsIntEntTimeOfCreation=_DsIntEntTimeOfCreation_Object((1,3,6,1,2,1,66,3,1,3),_DsIntEntTimeOfCreation_Type())
dsIntEntTimeOfCreation.setMaxAccess(_C)
if mibBuilder.loadTexts:dsIntEntTimeOfCreation.setStatus(_A)
_DsIntEntTimeOfLastAttempt_Type=TimeStamp
_DsIntEntTimeOfLastAttempt_Object=MibTableColumn
dsIntEntTimeOfLastAttempt=_DsIntEntTimeOfLastAttempt_Object((1,3,6,1,2,1,66,3,1,4),_DsIntEntTimeOfLastAttempt_Type())
dsIntEntTimeOfLastAttempt.setMaxAccess(_C)
if mibBuilder.loadTexts:dsIntEntTimeOfLastAttempt.setStatus(_A)
_DsIntEntTimeOfLastSuccess_Type=TimeStamp
_DsIntEntTimeOfLastSuccess_Object=MibTableColumn
dsIntEntTimeOfLastSuccess=_DsIntEntTimeOfLastSuccess_Object((1,3,6,1,2,1,66,3,1,5),_DsIntEntTimeOfLastSuccess_Type())
dsIntEntTimeOfLastSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:dsIntEntTimeOfLastSuccess.setStatus(_A)
_DsIntEntFailuresSinceLastSuccess_Type=Gauge32
_DsIntEntFailuresSinceLastSuccess_Object=MibTableColumn
dsIntEntFailuresSinceLastSuccess=_DsIntEntFailuresSinceLastSuccess_Object((1,3,6,1,2,1,66,3,1,6),_DsIntEntFailuresSinceLastSuccess_Type())
dsIntEntFailuresSinceLastSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:dsIntEntFailuresSinceLastSuccess.setStatus(_A)
_DsIntEntFailures_Type=ZeroBasedCounter32
_DsIntEntFailures_Object=MibTableColumn
dsIntEntFailures=_DsIntEntFailures_Object((1,3,6,1,2,1,66,3,1,7),_DsIntEntFailures_Type())
dsIntEntFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:dsIntEntFailures.setStatus(_A)
_DsIntEntSuccesses_Type=ZeroBasedCounter32
_DsIntEntSuccesses_Object=MibTableColumn
dsIntEntSuccesses=_DsIntEntSuccesses_Object((1,3,6,1,2,1,66,3,1,8),_DsIntEntSuccesses_Type())
dsIntEntSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:dsIntEntSuccesses.setStatus(_A)
_DsIntEntURL_Type=URLString
_DsIntEntURL_Object=MibTableColumn
dsIntEntURL=_DsIntEntURL_Object((1,3,6,1,2,1,66,3,1,9),_DsIntEntURL_Type())
dsIntEntURL.setMaxAccess(_C)
if mibBuilder.loadTexts:dsIntEntURL.setStatus(_A)
_DsConformance_ObjectIdentity=ObjectIdentity
dsConformance=_DsConformance_ObjectIdentity((1,3,6,1,2,1,66,4))
_DsGroups_ObjectIdentity=ObjectIdentity
dsGroups=_DsGroups_ObjectIdentity((1,3,6,1,2,1,66,4,1))
_DsCompliances_ObjectIdentity=ObjectIdentity
dsCompliances=_DsCompliances_ObjectIdentity((1,3,6,1,2,1,66,4,2))
dsEntryGroup=ObjectGroup((1,3,6,1,2,1,66,4,1,1))
dsEntryGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:dsEntryGroup.setStatus(_A)
dsOpsGroup=ObjectGroup((1,3,6,1,2,1,66,4,1,2))
dsOpsGroup.setObjects(*((_B,_G),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:dsOpsGroup.setStatus(_A)
dsIntGroup=ObjectGroup((1,3,6,1,2,1,66,4,1,3))
dsIntGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:dsIntGroup.setStatus(_A)
dsEntryCompliance=ModuleCompliance((1,3,6,1,2,1,66,4,2,1))
dsEntryCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:dsEntryCompliance.setStatus(_A)
dsOpsCompliance=ModuleCompliance((1,3,6,1,2,1,66,4,2,2))
dsOpsCompliance.setObjects(*((_B,_D),(_B,_I)))
if mibBuilder.loadTexts:dsOpsCompliance.setStatus(_A)
dsIntCompliance=ModuleCompliance((1,3,6,1,2,1,66,4,2,3))
dsIntCompliance.setObjects(*((_B,_D),(_B,_J)))
if mibBuilder.loadTexts:dsIntCompliance.setStatus(_A)
dsOpsIntCompliance=ModuleCompliance((1,3,6,1,2,1,66,4,2,4))
dsOpsIntCompliance.setObjects(*((_B,_D),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:dsOpsIntCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dsMIB':dsMIB,'dsTable':dsTable,'dsTableEntry':dsTableEntry,_L:dsServerType,_M:dsServerDescription,_N:dsMasterEntries,_O:dsCopyEntries,_P:dsCacheEntries,_Q:dsCacheHits,_R:dsSlaveHits,'dsApplIfOpsTable':dsApplIfOpsTable,'dsApplIfOpsEntry':dsApplIfOpsEntry,_G:dsApplIfProtocolIndex,_S:dsApplIfProtocol,_T:dsApplIfUnauthBinds,_U:dsApplIfSimpleAuthBinds,_V:dsApplIfStrongAuthBinds,_W:dsApplIfBindSecurityErrors,_X:dsApplIfInOps,_Y:dsApplIfReadOps,_Z:dsApplIfCompareOps,_a:dsApplIfAddEntryOps,_b:dsApplIfRemoveEntryOps,_c:dsApplIfModifyEntryOps,_d:dsApplIfModifyRDNOps,_e:dsApplIfListOps,_f:dsApplIfSearchOps,_g:dsApplIfOneLevelSearchOps,_h:dsApplIfWholeSubtreeSearchOps,_i:dsApplIfReferrals,_j:dsApplIfChainings,_k:dsApplIfSecurityErrors,_l:dsApplIfErrors,_m:dsApplIfReplicationUpdatesIn,_n:dsApplIfReplicationUpdatesOut,_o:dsApplIfInBytes,_p:dsApplIfOutBytes,'dsIntTable':dsIntTable,'dsIntEntry':dsIntEntry,_K:dsIntEntIndex,_q:dsIntEntDirectoryName,_r:dsIntEntTimeOfCreation,_s:dsIntEntTimeOfLastAttempt,_t:dsIntEntTimeOfLastSuccess,_u:dsIntEntFailuresSinceLastSuccess,_v:dsIntEntFailures,_w:dsIntEntSuccesses,_x:dsIntEntURL,'dsConformance':dsConformance,'dsGroups':dsGroups,_D:dsEntryGroup,_I:dsOpsGroup,_J:dsIntGroup,'dsCompliances':dsCompliances,'dsEntryCompliance':dsEntryCompliance,'dsOpsCompliance':dsOpsCompliance,'dsIntCompliance':dsIntCompliance,'dsOpsIntCompliance':dsOpsIntCompliance})