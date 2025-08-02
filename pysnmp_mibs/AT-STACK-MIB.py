_G='hostId'
_F='AT-SYSINFO-MIB'
_E='DisplayStringUnsized'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB',_E,'modules')
hostId,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
stack=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,120))
if mibBuilder.loadTexts:stack.setRevisions(('2006-05-03 09:26',))
class _StackId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_StackId_Type.__name__=_C
_StackId_Object=MibScalar
stackId=_StackId_Object((1,3,6,1,4,1,207,8,4,4,4,120,1),_StackId_Type())
stackId.setMaxAccess(_D)
if mibBuilder.loadTexts:stackId.setStatus(_A)
class _StackSnmpHost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_StackSnmpHost_Type.__name__=_C
_StackSnmpHost_Object=MibScalar
stackSnmpHost=_StackSnmpHost_Object((1,3,6,1,4,1,207,8,4,4,4,120,2),_StackSnmpHost_Type())
stackSnmpHost.setMaxAccess(_D)
if mibBuilder.loadTexts:stackSnmpHost.setStatus(_A)
class _StackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_StackStatus_Type.__name__=_C
_StackStatus_Object=MibScalar
stackStatus=_StackStatus_Object((1,3,6,1,4,1,207,8,4,4,4,120,3),_StackStatus_Type())
stackStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:stackStatus.setStatus(_A)
_StackInterface_Type=DisplayString
_StackInterface_Object=MibScalar
stackInterface=_StackInterface_Object((1,3,6,1,4,1,207,8,4,4,4,120,4),_StackInterface_Type())
stackInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:stackInterface.setStatus(_A)
class _StackAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('plaintext',1),('md5',2)))
_StackAuth_Type.__name__=_C
_StackAuth_Object=MibScalar
stackAuth=_StackAuth_Object((1,3,6,1,4,1,207,8,4,4,4,120,5),_StackAuth_Type())
stackAuth.setMaxAccess(_D)
if mibBuilder.loadTexts:stackAuth.setStatus(_A)
class _StackPassword_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_StackPassword_Type.__name__=_E
_StackPassword_Object=MibScalar
stackPassword=_StackPassword_Object((1,3,6,1,4,1,207,8,4,4,4,120,6),_StackPassword_Type())
stackPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:stackPassword.setStatus(_A)
_Counters_ObjectIdentity=ObjectIdentity
counters=_Counters_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,120,7))
_DebugErrors_Type=Integer32
_DebugErrors_Object=MibScalar
debugErrors=_DebugErrors_Object((1,3,6,1,4,1,207,8,4,4,4,120,7,1),_DebugErrors_Type())
debugErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:debugErrors.setStatus(_A)
_RxPkts_Type=Integer32
_RxPkts_Object=MibScalar
rxPkts=_RxPkts_Object((1,3,6,1,4,1,207,8,4,4,4,120,7,2),_RxPkts_Type())
rxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rxPkts.setStatus(_A)
_RxDiscards_Type=Integer32
_RxDiscards_Object=MibScalar
rxDiscards=_RxDiscards_Object((1,3,6,1,4,1,207,8,4,4,4,120,7,3),_RxDiscards_Type())
rxDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:rxDiscards.setStatus(_A)
_TxPkts_Type=Integer32
_TxPkts_Object=MibScalar
txPkts=_TxPkts_Object((1,3,6,1,4,1,207,8,4,4,4,120,7,4),_TxPkts_Type())
txPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:txPkts.setStatus(_A)
_TxFails_Type=Integer32
_TxFails_Object=MibScalar
txFails=_TxFails_Object((1,3,6,1,4,1,207,8,4,4,4,120,7,5),_TxFails_Type())
txFails.setMaxAccess(_B)
if mibBuilder.loadTexts:txFails.setStatus(_A)
_SdrCount_Type=Integer32
_SdrCount_Object=MibScalar
sdrCount=_SdrCount_Object((1,3,6,1,4,1,207,8,4,4,4,120,7,6),_SdrCount_Type())
sdrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sdrCount.setStatus(_A)
_StackMemberTable_Object=MibTable
stackMemberTable=_StackMemberTable_Object((1,3,6,1,4,1,207,8,4,4,4,120,8))
if mibBuilder.loadTexts:stackMemberTable.setStatus(_A)
_StackMemberEntry_Object=MibTableRow
stackMemberEntry=_StackMemberEntry_Object((1,3,6,1,4,1,207,8,4,4,4,120,8,1))
stackMemberEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:stackMemberEntry.setStatus(_A)
class _MemberHostId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_MemberHostId_Type.__name__=_C
_MemberHostId_Object=MibTableColumn
memberHostId=_MemberHostId_Object((1,3,6,1,4,1,207,8,4,4,4,120,8,1,1),_MemberHostId_Type())
memberHostId.setMaxAccess(_B)
if mibBuilder.loadTexts:memberHostId.setStatus(_A)
_MacAddress_Type=DisplayString
_MacAddress_Object=MibTableColumn
macAddress=_MacAddress_Object((1,3,6,1,4,1,207,8,4,4,4,120,8,1,2),_MacAddress_Type())
macAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:macAddress.setStatus(_A)
class _DedicatedMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DedicatedMaster_Type.__name__=_C
_DedicatedMaster_Object=MibTableColumn
dedicatedMaster=_DedicatedMaster_Object((1,3,6,1,4,1,207,8,4,4,4,120,8,1,3),_DedicatedMaster_Type())
dedicatedMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:dedicatedMaster.setStatus(_A)
class _BackupDedicatedMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BackupDedicatedMaster_Type.__name__=_C
_BackupDedicatedMaster_Object=MibTableColumn
backupDedicatedMaster=_BackupDedicatedMaster_Object((1,3,6,1,4,1,207,8,4,4,4,120,8,1,4),_BackupDedicatedMaster_Type())
backupDedicatedMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:backupDedicatedMaster.setStatus(_A)
_State_Type=DisplayString
_State_Object=MibTableColumn
state=_State_Object((1,3,6,1,4,1,207,8,4,4,4,120,8,1,5),_State_Type())
state.setMaxAccess(_B)
if mibBuilder.loadTexts:state.setStatus(_A)
mibBuilder.exportSymbols('AT-STACK-MIB',**{'stack':stack,'stackId':stackId,'stackSnmpHost':stackSnmpHost,'stackStatus':stackStatus,'stackInterface':stackInterface,'stackAuth':stackAuth,'stackPassword':stackPassword,'counters':counters,'debugErrors':debugErrors,'rxPkts':rxPkts,'rxDiscards':rxDiscards,'txPkts':txPkts,'txFails':txFails,'sdrCount':sdrCount,'stackMemberTable':stackMemberTable,'stackMemberEntry':stackMemberEntry,'memberHostId':memberHostId,'macAddress':macAddress,'dedicatedMaster':dedicatedMaster,'backupDedicatedMaster':backupDedicatedMaster,'state':state})