_F='mellanoxSWPartitionIndex'
_E='MELLANOX-SW-UPDATE-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mellanoxSWUpdate,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxSWUpdate')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxSWUpdateMib=ModuleIdentity((1,3,6,1,4,1,33049,11,1))
if mibBuilder.loadTexts:mellanoxSWUpdateMib.setRevisions(('2017-07-25 00:00',))
_MellanoxSWUpdateMibObjects_ObjectIdentity=ObjectIdentity
mellanoxSWUpdateMibObjects=_MellanoxSWUpdateMibObjects_ObjectIdentity((1,3,6,1,4,1,33049,11,1,1))
_MellanoxSWTable_Object=MibTable
mellanoxSWTable=_MellanoxSWTable_Object((1,3,6,1,4,1,33049,11,1,1,1))
if mibBuilder.loadTexts:mellanoxSWTable.setStatus(_A)
_MellanoxSWEntry_Object=MibTableRow
mellanoxSWEntry=_MellanoxSWEntry_Object((1,3,6,1,4,1,33049,11,1,1,1,1))
mellanoxSWEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mellanoxSWEntry.setStatus(_A)
_MellanoxSWPartitionIndex_Type=Integer32
_MellanoxSWPartitionIndex_Object=MibTableColumn
mellanoxSWPartitionIndex=_MellanoxSWPartitionIndex_Object((1,3,6,1,4,1,33049,11,1,1,1,1,1),_MellanoxSWPartitionIndex_Type())
mellanoxSWPartitionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxSWPartitionIndex.setStatus(_A)
_MellanoxSWPartitionName_Type=OctetString
_MellanoxSWPartitionName_Object=MibTableColumn
mellanoxSWPartitionName=_MellanoxSWPartitionName_Object((1,3,6,1,4,1,33049,11,1,1,1,1,2),_MellanoxSWPartitionName_Type())
mellanoxSWPartitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxSWPartitionName.setStatus(_A)
_MellanoxSWPartitionActive_Type=Integer32
_MellanoxSWPartitionActive_Object=MibTableColumn
mellanoxSWPartitionActive=_MellanoxSWPartitionActive_Object((1,3,6,1,4,1,33049,11,1,1,1,1,3),_MellanoxSWPartitionActive_Type())
mellanoxSWPartitionActive.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxSWPartitionActive.setStatus(_A)
_MellanoxSWPartitionBootNext_Type=Integer32
_MellanoxSWPartitionBootNext_Object=MibTableColumn
mellanoxSWPartitionBootNext=_MellanoxSWPartitionBootNext_Object((1,3,6,1,4,1,33049,11,1,1,1,1,4),_MellanoxSWPartitionBootNext_Type())
mellanoxSWPartitionBootNext.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxSWPartitionBootNext.setStatus(_A)
_MellanoxSWUpdateCmd_ObjectIdentity=ObjectIdentity
mellanoxSWUpdateCmd=_MellanoxSWUpdateCmd_ObjectIdentity((1,3,6,1,4,1,33049,11,1,1,2))
_MellanoxSWUpdateCmdSetNext_Type=Integer32
_MellanoxSWUpdateCmdSetNext_Object=MibScalar
mellanoxSWUpdateCmdSetNext=_MellanoxSWUpdateCmdSetNext_Object((1,3,6,1,4,1,33049,11,1,1,2,1),_MellanoxSWUpdateCmdSetNext_Type())
mellanoxSWUpdateCmdSetNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mellanoxSWUpdateCmdSetNext.setStatus(_A)
_MellanoxSWUpdateCmdUri_Type=OctetString
_MellanoxSWUpdateCmdUri_Object=MibScalar
mellanoxSWUpdateCmdUri=_MellanoxSWUpdateCmdUri_Object((1,3,6,1,4,1,33049,11,1,1,2,2),_MellanoxSWUpdateCmdUri_Type())
mellanoxSWUpdateCmdUri.setMaxAccess(_C)
if mibBuilder.loadTexts:mellanoxSWUpdateCmdUri.setStatus(_A)
class _MellanoxSWUpdateCmdExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mellanoxSWUpdateCmdExecuteUpdate',1),('mellanoxSWUpdateCmdExecuteSetNext',2)))
_MellanoxSWUpdateCmdExecute_Type.__name__=_D
_MellanoxSWUpdateCmdExecute_Object=MibScalar
mellanoxSWUpdateCmdExecute=_MellanoxSWUpdateCmdExecute_Object((1,3,6,1,4,1,33049,11,1,1,2,3),_MellanoxSWUpdateCmdExecute_Type())
mellanoxSWUpdateCmdExecute.setMaxAccess(_C)
if mibBuilder.loadTexts:mellanoxSWUpdateCmdExecute.setStatus(_A)
_MellanoxSWUpdateCmdStatus_Type=Integer32
_MellanoxSWUpdateCmdStatus_Object=MibScalar
mellanoxSWUpdateCmdStatus=_MellanoxSWUpdateCmdStatus_Object((1,3,6,1,4,1,33049,11,1,1,2,4),_MellanoxSWUpdateCmdStatus_Type())
mellanoxSWUpdateCmdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxSWUpdateCmdStatus.setStatus(_A)
_MellanoxSWUpdateCmdStatusString_Type=OctetString
_MellanoxSWUpdateCmdStatusString_Object=MibScalar
mellanoxSWUpdateCmdStatusString=_MellanoxSWUpdateCmdStatusString_Object((1,3,6,1,4,1,33049,11,1,1,2,5),_MellanoxSWUpdateCmdStatusString_Type())
mellanoxSWUpdateCmdStatusString.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxSWUpdateCmdStatusString.setStatus(_A)
_MellanoxSWActivePartition_Type=Integer32
_MellanoxSWActivePartition_Object=MibScalar
mellanoxSWActivePartition=_MellanoxSWActivePartition_Object((1,3,6,1,4,1,33049,11,1,1,3),_MellanoxSWActivePartition_Type())
mellanoxSWActivePartition.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxSWActivePartition.setStatus(_A)
_MellanoxSWNextBootPartition_Type=Integer32
_MellanoxSWNextBootPartition_Object=MibScalar
mellanoxSWNextBootPartition=_MellanoxSWNextBootPartition_Object((1,3,6,1,4,1,33049,11,1,1,4),_MellanoxSWNextBootPartition_Type())
mellanoxSWNextBootPartition.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxSWNextBootPartition.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mellanoxSWUpdateMib':mellanoxSWUpdateMib,'mellanoxSWUpdateMibObjects':mellanoxSWUpdateMibObjects,'mellanoxSWTable':mellanoxSWTable,'mellanoxSWEntry':mellanoxSWEntry,_F:mellanoxSWPartitionIndex,'mellanoxSWPartitionName':mellanoxSWPartitionName,'mellanoxSWPartitionActive':mellanoxSWPartitionActive,'mellanoxSWPartitionBootNext':mellanoxSWPartitionBootNext,'mellanoxSWUpdateCmd':mellanoxSWUpdateCmd,'mellanoxSWUpdateCmdSetNext':mellanoxSWUpdateCmdSetNext,'mellanoxSWUpdateCmdUri':mellanoxSWUpdateCmdUri,'mellanoxSWUpdateCmdExecute':mellanoxSWUpdateCmdExecute,'mellanoxSWUpdateCmdStatus':mellanoxSWUpdateCmdStatus,'mellanoxSWUpdateCmdStatusString':mellanoxSWUpdateCmdStatusString,'mellanoxSWActivePartition':mellanoxSWActivePartition,'mellanoxSWNextBootPartition':mellanoxSWNextBootPartition})