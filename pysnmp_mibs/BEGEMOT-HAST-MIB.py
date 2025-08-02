_E='hastResourceIndex'
_D='BEGEMOT-HAST-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
begemotHast=ModuleIdentity((1,3,6,1,4,1,12325,1,220))
if mibBuilder.loadTexts:begemotHast.setRevisions(('2013-04-13 00:00','2013-07-01 00:00','2013-12-29 00:00'))
_BegemotHastObjects_ObjectIdentity=ObjectIdentity
begemotHastObjects=_BegemotHastObjects_ObjectIdentity((1,3,6,1,4,1,12325,1,220,1))
_HastConfig_ObjectIdentity=ObjectIdentity
hastConfig=_HastConfig_ObjectIdentity((1,3,6,1,4,1,12325,1,220,1,1))
_HastConfigFile_Type=OctetString
_HastConfigFile_Object=MibScalar
hastConfigFile=_HastConfigFile_Object((1,3,6,1,4,1,12325,1,220,1,1,1),_HastConfigFile_Type())
hastConfigFile.setMaxAccess(_B)
if mibBuilder.loadTexts:hastConfigFile.setStatus(_A)
_HastResourceTable_Object=MibTable
hastResourceTable=_HastResourceTable_Object((1,3,6,1,4,1,12325,1,220,1,2))
if mibBuilder.loadTexts:hastResourceTable.setStatus(_A)
_HastResourceEntry_Object=MibTableRow
hastResourceEntry=_HastResourceEntry_Object((1,3,6,1,4,1,12325,1,220,1,2,1))
hastResourceEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hastResourceEntry.setStatus(_A)
_HastResourceIndex_Type=Integer32
_HastResourceIndex_Object=MibTableColumn
hastResourceIndex=_HastResourceIndex_Object((1,3,6,1,4,1,12325,1,220,1,2,1,1),_HastResourceIndex_Type())
hastResourceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceIndex.setStatus(_A)
_HastResourceName_Type=OctetString
_HastResourceName_Object=MibTableColumn
hastResourceName=_HastResourceName_Object((1,3,6,1,4,1,12325,1,220,1,2,1,2),_HastResourceName_Type())
hastResourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceName.setStatus(_A)
class _HastResourceRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('undef',0),('init',1),('primary',2),('secondary',3)))
_HastResourceRole_Type.__name__=_C
_HastResourceRole_Object=MibTableColumn
hastResourceRole=_HastResourceRole_Object((1,3,6,1,4,1,12325,1,220,1,2,1,3),_HastResourceRole_Type())
hastResourceRole.setMaxAccess('read-write')
if mibBuilder.loadTexts:hastResourceRole.setStatus(_A)
_HastResourceProvName_Type=OctetString
_HastResourceProvName_Object=MibTableColumn
hastResourceProvName=_HastResourceProvName_Object((1,3,6,1,4,1,12325,1,220,1,2,1,4),_HastResourceProvName_Type())
hastResourceProvName.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceProvName.setStatus(_A)
_HastResourceLocalPath_Type=OctetString
_HastResourceLocalPath_Object=MibTableColumn
hastResourceLocalPath=_HastResourceLocalPath_Object((1,3,6,1,4,1,12325,1,220,1,2,1,5),_HastResourceLocalPath_Type())
hastResourceLocalPath.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceLocalPath.setStatus(_A)
_HastResourceExtentSize_Type=Integer32
_HastResourceExtentSize_Object=MibTableColumn
hastResourceExtentSize=_HastResourceExtentSize_Object((1,3,6,1,4,1,12325,1,220,1,2,1,6),_HastResourceExtentSize_Type())
hastResourceExtentSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceExtentSize.setStatus(_A)
_HastResourceKeepDirty_Type=Integer32
_HastResourceKeepDirty_Object=MibTableColumn
hastResourceKeepDirty=_HastResourceKeepDirty_Object((1,3,6,1,4,1,12325,1,220,1,2,1,7),_HastResourceKeepDirty_Type())
hastResourceKeepDirty.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceKeepDirty.setStatus(_A)
_HastResourceRemoteAddr_Type=OctetString
_HastResourceRemoteAddr_Object=MibTableColumn
hastResourceRemoteAddr=_HastResourceRemoteAddr_Object((1,3,6,1,4,1,12325,1,220,1,2,1,8),_HastResourceRemoteAddr_Type())
hastResourceRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceRemoteAddr.setStatus(_A)
_HastResourceSourceAddr_Type=OctetString
_HastResourceSourceAddr_Object=MibTableColumn
hastResourceSourceAddr=_HastResourceSourceAddr_Object((1,3,6,1,4,1,12325,1,220,1,2,1,9),_HastResourceSourceAddr_Type())
hastResourceSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceSourceAddr.setStatus(_A)
class _HastResourceReplication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('fullsync',0),('memsync',1),('async',2)))
_HastResourceReplication_Type.__name__=_C
_HastResourceReplication_Object=MibTableColumn
hastResourceReplication=_HastResourceReplication_Object((1,3,6,1,4,1,12325,1,220,1,2,1,10),_HastResourceReplication_Type())
hastResourceReplication.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceReplication.setStatus(_A)
class _HastResourceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('complete',0),('degraded',1)))
_HastResourceStatus_Type.__name__=_C
_HastResourceStatus_Object=MibTableColumn
hastResourceStatus=_HastResourceStatus_Object((1,3,6,1,4,1,12325,1,220,1,2,1,11),_HastResourceStatus_Type())
hastResourceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceStatus.setStatus(_A)
_HastResourceDirty_Type=Counter64
_HastResourceDirty_Object=MibTableColumn
hastResourceDirty=_HastResourceDirty_Object((1,3,6,1,4,1,12325,1,220,1,2,1,12),_HastResourceDirty_Type())
hastResourceDirty.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceDirty.setStatus(_A)
_HastResourceReads_Type=Counter64
_HastResourceReads_Object=MibTableColumn
hastResourceReads=_HastResourceReads_Object((1,3,6,1,4,1,12325,1,220,1,2,1,13),_HastResourceReads_Type())
hastResourceReads.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceReads.setStatus(_A)
_HastResourceWrites_Type=Counter64
_HastResourceWrites_Object=MibTableColumn
hastResourceWrites=_HastResourceWrites_Object((1,3,6,1,4,1,12325,1,220,1,2,1,14),_HastResourceWrites_Type())
hastResourceWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceWrites.setStatus(_A)
_HastResourceDeletes_Type=Counter64
_HastResourceDeletes_Object=MibTableColumn
hastResourceDeletes=_HastResourceDeletes_Object((1,3,6,1,4,1,12325,1,220,1,2,1,15),_HastResourceDeletes_Type())
hastResourceDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceDeletes.setStatus(_A)
_HastResourceFlushes_Type=Counter64
_HastResourceFlushes_Object=MibTableColumn
hastResourceFlushes=_HastResourceFlushes_Object((1,3,6,1,4,1,12325,1,220,1,2,1,16),_HastResourceFlushes_Type())
hastResourceFlushes.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceFlushes.setStatus(_A)
_HastResourceActivemapUpdates_Type=Counter64
_HastResourceActivemapUpdates_Object=MibTableColumn
hastResourceActivemapUpdates=_HastResourceActivemapUpdates_Object((1,3,6,1,4,1,12325,1,220,1,2,1,17),_HastResourceActivemapUpdates_Type())
hastResourceActivemapUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceActivemapUpdates.setStatus(_A)
_HastResourceReadErrors_Type=Counter64
_HastResourceReadErrors_Object=MibTableColumn
hastResourceReadErrors=_HastResourceReadErrors_Object((1,3,6,1,4,1,12325,1,220,1,2,1,18),_HastResourceReadErrors_Type())
hastResourceReadErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceReadErrors.setStatus(_A)
_HastResourceWriteErrors_Type=Counter64
_HastResourceWriteErrors_Object=MibTableColumn
hastResourceWriteErrors=_HastResourceWriteErrors_Object((1,3,6,1,4,1,12325,1,220,1,2,1,19),_HastResourceWriteErrors_Type())
hastResourceWriteErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceWriteErrors.setStatus(_A)
_HastResourceDeleteErrors_Type=Counter64
_HastResourceDeleteErrors_Object=MibTableColumn
hastResourceDeleteErrors=_HastResourceDeleteErrors_Object((1,3,6,1,4,1,12325,1,220,1,2,1,20),_HastResourceDeleteErrors_Type())
hastResourceDeleteErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceDeleteErrors.setStatus(_A)
_HastResourceFlushErrors_Type=Counter64
_HastResourceFlushErrors_Object=MibTableColumn
hastResourceFlushErrors=_HastResourceFlushErrors_Object((1,3,6,1,4,1,12325,1,220,1,2,1,21),_HastResourceFlushErrors_Type())
hastResourceFlushErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceFlushErrors.setStatus(_A)
_HastResourceWorkerPid_Type=Integer32
_HastResourceWorkerPid_Object=MibTableColumn
hastResourceWorkerPid=_HastResourceWorkerPid_Object((1,3,6,1,4,1,12325,1,220,1,2,1,22),_HastResourceWorkerPid_Type())
hastResourceWorkerPid.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceWorkerPid.setStatus(_A)
_HastResourceLocalQueue_Type=Unsigned32
_HastResourceLocalQueue_Object=MibTableColumn
hastResourceLocalQueue=_HastResourceLocalQueue_Object((1,3,6,1,4,1,12325,1,220,1,2,1,23),_HastResourceLocalQueue_Type())
hastResourceLocalQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceLocalQueue.setStatus(_A)
_HastResourceSendQueue_Type=Unsigned32
_HastResourceSendQueue_Object=MibTableColumn
hastResourceSendQueue=_HastResourceSendQueue_Object((1,3,6,1,4,1,12325,1,220,1,2,1,24),_HastResourceSendQueue_Type())
hastResourceSendQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceSendQueue.setStatus(_A)
_HastResourceRecvQueue_Type=Unsigned32
_HastResourceRecvQueue_Object=MibTableColumn
hastResourceRecvQueue=_HastResourceRecvQueue_Object((1,3,6,1,4,1,12325,1,220,1,2,1,25),_HastResourceRecvQueue_Type())
hastResourceRecvQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceRecvQueue.setStatus(_A)
_HastResourceDoneQueue_Type=Unsigned32
_HastResourceDoneQueue_Object=MibTableColumn
hastResourceDoneQueue=_HastResourceDoneQueue_Object((1,3,6,1,4,1,12325,1,220,1,2,1,26),_HastResourceDoneQueue_Type())
hastResourceDoneQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceDoneQueue.setStatus(_A)
_HastResourceIdleQueue_Type=Unsigned32
_HastResourceIdleQueue_Object=MibTableColumn
hastResourceIdleQueue=_HastResourceIdleQueue_Object((1,3,6,1,4,1,12325,1,220,1,2,1,27),_HastResourceIdleQueue_Type())
hastResourceIdleQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:hastResourceIdleQueue.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'begemotHast':begemotHast,'begemotHastObjects':begemotHastObjects,'hastConfig':hastConfig,'hastConfigFile':hastConfigFile,'hastResourceTable':hastResourceTable,'hastResourceEntry':hastResourceEntry,_E:hastResourceIndex,'hastResourceName':hastResourceName,'hastResourceRole':hastResourceRole,'hastResourceProvName':hastResourceProvName,'hastResourceLocalPath':hastResourceLocalPath,'hastResourceExtentSize':hastResourceExtentSize,'hastResourceKeepDirty':hastResourceKeepDirty,'hastResourceRemoteAddr':hastResourceRemoteAddr,'hastResourceSourceAddr':hastResourceSourceAddr,'hastResourceReplication':hastResourceReplication,'hastResourceStatus':hastResourceStatus,'hastResourceDirty':hastResourceDirty,'hastResourceReads':hastResourceReads,'hastResourceWrites':hastResourceWrites,'hastResourceDeletes':hastResourceDeletes,'hastResourceFlushes':hastResourceFlushes,'hastResourceActivemapUpdates':hastResourceActivemapUpdates,'hastResourceReadErrors':hastResourceReadErrors,'hastResourceWriteErrors':hastResourceWriteErrors,'hastResourceDeleteErrors':hastResourceDeleteErrors,'hastResourceFlushErrors':hastResourceFlushErrors,'hastResourceWorkerPid':hastResourceWorkerPid,'hastResourceLocalQueue':hastResourceLocalQueue,'hastResourceSendQueue':hastResourceSendQueue,'hastResourceRecvQueue':hastResourceRecvQueue,'hastResourceDoneQueue':hastResourceDoneQueue,'hastResourceIdleQueue':hastResourceIdleQueue})