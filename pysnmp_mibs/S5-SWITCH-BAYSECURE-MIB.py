_g='read-create'
_f='s5SbsDaFilteringIndx'
_e='s5SbsAutoLearningConfigPort'
_d='s5SbsAutoLearningConfigBrd'
_c='s5SbsMacViolationAddress'
_b='s5SbsSecurityListIndx'
_a='s5SbsViolationStatusPortIndx'
_Z='s5SbsViolationStatusBrdIndx'
_Y='s5SbsAuthStatusMACIndx'
_X='s5SbsAuthStatusPortIndx'
_W='s5SbsAuthStatusBrdIndx'
_V='modify'
_U='delete'
_T='create'
_S='s5SbsAuthCfgMACIndx'
_R='s5SbsAuthCfgPortIndx'
_Q='s5SbsAuthCfgBrdIndx'
_P='partitionPortdaFilteringAndsendTrap'
_O='partitionPortAnddaFiltering'
_N='daFilteringAndsendTrap'
_M='daFiltering'
_L='partitionPortAndsendTrap'
_K='partitionPort'
_J='noAction'
_I='autoLearn'
_H='TruthValue'
_G='not-accessible'
_F='valid'
_E='S5-SWITCH-BAYSECURE-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
s5Com,=mibBuilder.importSymbols('S5-ROOT-MIB','s5Com')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeInterval',_H)
s5SbsAuth=ModuleIdentity((1,3,6,1,4,1,45,1,6,5,3))
if mibBuilder.loadTexts:s5SbsAuth.setRevisions(('2016-05-18 00:00','2012-09-13 00:00','2011-01-10 00:00','2009-05-28 00:00','2009-02-24 00:00','2006-09-18 00:00','2005-03-09 00:00','2004-09-03 00:00','2004-07-22 00:00','2004-07-20 00:00','2003-02-20 00:00'))
class PortSet(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class _S5SbsAuthSecurityLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('locked',2),('notlocked',3)))
_S5SbsAuthSecurityLock_Type.__name__=_B
_S5SbsAuthSecurityLock_Object=MibScalar
s5SbsAuthSecurityLock=_S5SbsAuthSecurityLock_Object((1,3,6,1,4,1,45,1,6,5,3,1),_S5SbsAuthSecurityLock_Type())
s5SbsAuthSecurityLock.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsAuthSecurityLock.setStatus(_A)
class _S5SbsAuthCtlPartTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsAuthCtlPartTime_Type.__name__=_B
_S5SbsAuthCtlPartTime_Object=MibScalar
s5SbsAuthCtlPartTime=_S5SbsAuthCtlPartTime_Object((1,3,6,1,4,1,45,1,6,5,3,2),_S5SbsAuthCtlPartTime_Type())
s5SbsAuthCtlPartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAuthCtlPartTime.setStatus(_A)
class _S5SbsSecurityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_S5SbsSecurityStatus_Type.__name__=_B
_S5SbsSecurityStatus_Object=MibScalar
s5SbsSecurityStatus=_S5SbsSecurityStatus_Object((1,3,6,1,4,1,45,1,6,5,3,3),_S5SbsSecurityStatus_Type())
s5SbsSecurityStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsSecurityStatus.setStatus(_A)
class _S5SbsSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('singleMACperPort',1),('macList',2),(_I,3)))
_S5SbsSecurityMode_Type.__name__=_B
_S5SbsSecurityMode_Object=MibScalar
s5SbsSecurityMode=_S5SbsSecurityMode_Object((1,3,6,1,4,1,45,1,6,5,3,4),_S5SbsSecurityMode_Type())
s5SbsSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsSecurityMode.setStatus(_A)
class _S5SbsSecurityAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),('trap',2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8)))
_S5SbsSecurityAction_Type.__name__=_B
_S5SbsSecurityAction_Object=MibScalar
s5SbsSecurityAction=_S5SbsSecurityAction_Object((1,3,6,1,4,1,45,1,6,5,3,5),_S5SbsSecurityAction_Type())
s5SbsSecurityAction.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsSecurityAction.setStatus(_A)
class _S5SbsCurrNodesAllowed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_S5SbsCurrNodesAllowed_Type.__name__=_B
_S5SbsCurrNodesAllowed_Object=MibScalar
s5SbsCurrNodesAllowed=_S5SbsCurrNodesAllowed_Object((1,3,6,1,4,1,45,1,6,5,3,6),_S5SbsCurrNodesAllowed_Type())
s5SbsCurrNodesAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsCurrNodesAllowed.setStatus(_A)
class _S5SbsMaxNodesAllowed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_S5SbsMaxNodesAllowed_Type.__name__=_B
_S5SbsMaxNodesAllowed_Object=MibScalar
s5SbsMaxNodesAllowed=_S5SbsMaxNodesAllowed_Object((1,3,6,1,4,1,45,1,6,5,3,7),_S5SbsMaxNodesAllowed_Type())
s5SbsMaxNodesAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsMaxNodesAllowed.setStatus(_A)
class _S5SbsCurrNodesBlocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_S5SbsCurrNodesBlocked_Type.__name__=_B
_S5SbsCurrNodesBlocked_Object=MibScalar
s5SbsCurrNodesBlocked=_S5SbsCurrNodesBlocked_Object((1,3,6,1,4,1,45,1,6,5,3,8),_S5SbsCurrNodesBlocked_Type())
s5SbsCurrNodesBlocked.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsCurrNodesBlocked.setStatus(_A)
class _S5SbsMaxNodesBlocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_S5SbsMaxNodesBlocked_Type.__name__=_B
_S5SbsMaxNodesBlocked_Object=MibScalar
s5SbsMaxNodesBlocked=_S5SbsMaxNodesBlocked_Object((1,3,6,1,4,1,45,1,6,5,3,9),_S5SbsMaxNodesBlocked_Type())
s5SbsMaxNodesBlocked.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsMaxNodesBlocked.setStatus(_A)
_S5SbsAuthCfgTable_Object=MibTable
s5SbsAuthCfgTable=_S5SbsAuthCfgTable_Object((1,3,6,1,4,1,45,1,6,5,3,10))
if mibBuilder.loadTexts:s5SbsAuthCfgTable.setStatus(_A)
_S5SbsAuthCfgEntry_Object=MibTableRow
s5SbsAuthCfgEntry=_S5SbsAuthCfgEntry_Object((1,3,6,1,4,1,45,1,6,5,3,10,1))
s5SbsAuthCfgEntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:s5SbsAuthCfgEntry.setStatus(_A)
class _S5SbsAuthCfgBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsAuthCfgBrdIndx_Type.__name__=_B
_S5SbsAuthCfgBrdIndx_Object=MibTableColumn
s5SbsAuthCfgBrdIndx=_S5SbsAuthCfgBrdIndx_Object((1,3,6,1,4,1,45,1,6,5,3,10,1,1),_S5SbsAuthCfgBrdIndx_Type())
s5SbsAuthCfgBrdIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsAuthCfgBrdIndx.setStatus(_A)
class _S5SbsAuthCfgPortIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsAuthCfgPortIndx_Type.__name__=_B
_S5SbsAuthCfgPortIndx_Object=MibTableColumn
s5SbsAuthCfgPortIndx=_S5SbsAuthCfgPortIndx_Object((1,3,6,1,4,1,45,1,6,5,3,10,1,2),_S5SbsAuthCfgPortIndx_Type())
s5SbsAuthCfgPortIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsAuthCfgPortIndx.setStatus(_A)
_S5SbsAuthCfgMACIndx_Type=MacAddress
_S5SbsAuthCfgMACIndx_Object=MibTableColumn
s5SbsAuthCfgMACIndx=_S5SbsAuthCfgMACIndx_Object((1,3,6,1,4,1,45,1,6,5,3,10,1,3),_S5SbsAuthCfgMACIndx_Type())
s5SbsAuthCfgMACIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsAuthCfgMACIndx.setStatus(_A)
class _S5SbsAuthCfgAccessCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allowed',1),('blocked',2)))
_S5SbsAuthCfgAccessCtrlType_Type.__name__=_B
_S5SbsAuthCfgAccessCtrlType_Object=MibTableColumn
s5SbsAuthCfgAccessCtrlType=_S5SbsAuthCfgAccessCtrlType_Object((1,3,6,1,4,1,45,1,6,5,3,10,1,4),_S5SbsAuthCfgAccessCtrlType_Type())
s5SbsAuthCfgAccessCtrlType.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAuthCfgAccessCtrlType.setStatus(_A)
class _S5SbsAuthCfgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_T,2),(_U,3),(_V,4),('createSticky',5)))
_S5SbsAuthCfgStatus_Type.__name__=_B
_S5SbsAuthCfgStatus_Object=MibTableColumn
s5SbsAuthCfgStatus=_S5SbsAuthCfgStatus_Object((1,3,6,1,4,1,45,1,6,5,3,10,1,5),_S5SbsAuthCfgStatus_Type())
s5SbsAuthCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAuthCfgStatus.setStatus(_A)
class _S5SbsAuthCfgSecureList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsAuthCfgSecureList_Type.__name__=_B
_S5SbsAuthCfgSecureList_Object=MibTableColumn
s5SbsAuthCfgSecureList=_S5SbsAuthCfgSecureList_Object((1,3,6,1,4,1,45,1,6,5,3,10,1,6),_S5SbsAuthCfgSecureList_Type())
s5SbsAuthCfgSecureList.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAuthCfgSecureList.setStatus(_A)
class _S5SbsAuthCfgSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),(_I,2),('sticky',3)))
_S5SbsAuthCfgSource_Type.__name__=_B
_S5SbsAuthCfgSource_Object=MibTableColumn
s5SbsAuthCfgSource=_S5SbsAuthCfgSource_Object((1,3,6,1,4,1,45,1,6,5,3,10,1,7),_S5SbsAuthCfgSource_Type())
s5SbsAuthCfgSource.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsAuthCfgSource.setStatus(_A)
_S5SbsAuthCfgLifetime_Type=TimeInterval
_S5SbsAuthCfgLifetime_Object=MibTableColumn
s5SbsAuthCfgLifetime=_S5SbsAuthCfgLifetime_Object((1,3,6,1,4,1,45,1,6,5,3,10,1,8),_S5SbsAuthCfgLifetime_Type())
s5SbsAuthCfgLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsAuthCfgLifetime.setStatus(_A)
class _S5SbsAuthCfgTrunk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_S5SbsAuthCfgTrunk_Type.__name__=_B
_S5SbsAuthCfgTrunk_Object=MibTableColumn
s5SbsAuthCfgTrunk=_S5SbsAuthCfgTrunk_Object((1,3,6,1,4,1,45,1,6,5,3,10,1,9),_S5SbsAuthCfgTrunk_Type())
s5SbsAuthCfgTrunk.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAuthCfgTrunk.setStatus(_A)
_S5SbsAuthStatusTable_Object=MibTable
s5SbsAuthStatusTable=_S5SbsAuthStatusTable_Object((1,3,6,1,4,1,45,1,6,5,3,11))
if mibBuilder.loadTexts:s5SbsAuthStatusTable.setStatus(_A)
_S5SbsAuthStatusEntry_Object=MibTableRow
s5SbsAuthStatusEntry=_S5SbsAuthStatusEntry_Object((1,3,6,1,4,1,45,1,6,5,3,11,1))
s5SbsAuthStatusEntry.setIndexNames((0,_E,_W),(0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:s5SbsAuthStatusEntry.setStatus(_A)
class _S5SbsAuthStatusBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5SbsAuthStatusBrdIndx_Type.__name__=_B
_S5SbsAuthStatusBrdIndx_Object=MibTableColumn
s5SbsAuthStatusBrdIndx=_S5SbsAuthStatusBrdIndx_Object((1,3,6,1,4,1,45,1,6,5,3,11,1,1),_S5SbsAuthStatusBrdIndx_Type())
s5SbsAuthStatusBrdIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsAuthStatusBrdIndx.setStatus(_A)
class _S5SbsAuthStatusPortIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5SbsAuthStatusPortIndx_Type.__name__=_B
_S5SbsAuthStatusPortIndx_Object=MibTableColumn
s5SbsAuthStatusPortIndx=_S5SbsAuthStatusPortIndx_Object((1,3,6,1,4,1,45,1,6,5,3,11,1,2),_S5SbsAuthStatusPortIndx_Type())
s5SbsAuthStatusPortIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsAuthStatusPortIndx.setStatus(_A)
_S5SbsAuthStatusMACIndx_Type=MacAddress
_S5SbsAuthStatusMACIndx_Object=MibTableColumn
s5SbsAuthStatusMACIndx=_S5SbsAuthStatusMACIndx_Object((1,3,6,1,4,1,45,1,6,5,3,11,1,3),_S5SbsAuthStatusMACIndx_Type())
s5SbsAuthStatusMACIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsAuthStatusMACIndx.setStatus(_A)
class _S5SbsCurrentAccessCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('block',2)))
_S5SbsCurrentAccessCtrlType_Type.__name__=_B
_S5SbsCurrentAccessCtrlType_Object=MibTableColumn
s5SbsCurrentAccessCtrlType=_S5SbsCurrentAccessCtrlType_Object((1,3,6,1,4,1,45,1,6,5,3,11,1,4),_S5SbsCurrentAccessCtrlType_Type())
s5SbsCurrentAccessCtrlType.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsCurrentAccessCtrlType.setStatus(_A)
class _S5SbsCurrentActionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),('sendTrap',6),(_O,7),(_P,8)))
_S5SbsCurrentActionMode_Type.__name__=_B
_S5SbsCurrentActionMode_Object=MibTableColumn
s5SbsCurrentActionMode=_S5SbsCurrentActionMode_Object((1,3,6,1,4,1,45,1,6,5,3,11,1,5),_S5SbsCurrentActionMode_Type())
s5SbsCurrentActionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsCurrentActionMode.setStatus(_A)
class _S5SbsCurrentPortSecurStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('portSecure',2),('portPartition',3)))
_S5SbsCurrentPortSecurStatus_Type.__name__=_B
_S5SbsCurrentPortSecurStatus_Object=MibTableColumn
s5SbsCurrentPortSecurStatus=_S5SbsCurrentPortSecurStatus_Object((1,3,6,1,4,1,45,1,6,5,3,11,1,6),_S5SbsCurrentPortSecurStatus_Type())
s5SbsCurrentPortSecurStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsCurrentPortSecurStatus.setStatus(_A)
_S5SbsViolationStatusTable_Object=MibTable
s5SbsViolationStatusTable=_S5SbsViolationStatusTable_Object((1,3,6,1,4,1,45,1,6,5,3,12))
if mibBuilder.loadTexts:s5SbsViolationStatusTable.setStatus(_A)
_S5SbsViolationStatusEntry_Object=MibTableRow
s5SbsViolationStatusEntry=_S5SbsViolationStatusEntry_Object((1,3,6,1,4,1,45,1,6,5,3,12,1))
s5SbsViolationStatusEntry.setIndexNames((0,_E,_Z),(0,_E,_a))
if mibBuilder.loadTexts:s5SbsViolationStatusEntry.setStatus(_A)
class _S5SbsViolationStatusBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5SbsViolationStatusBrdIndx_Type.__name__=_B
_S5SbsViolationStatusBrdIndx_Object=MibTableColumn
s5SbsViolationStatusBrdIndx=_S5SbsViolationStatusBrdIndx_Object((1,3,6,1,4,1,45,1,6,5,3,12,1,1),_S5SbsViolationStatusBrdIndx_Type())
s5SbsViolationStatusBrdIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsViolationStatusBrdIndx.setStatus(_A)
class _S5SbsViolationStatusPortIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5SbsViolationStatusPortIndx_Type.__name__=_B
_S5SbsViolationStatusPortIndx_Object=MibTableColumn
s5SbsViolationStatusPortIndx=_S5SbsViolationStatusPortIndx_Object((1,3,6,1,4,1,45,1,6,5,3,12,1,2),_S5SbsViolationStatusPortIndx_Type())
s5SbsViolationStatusPortIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsViolationStatusPortIndx.setStatus(_A)
_S5SbsViolationStatusMACAddress_Type=MacAddress
_S5SbsViolationStatusMACAddress_Object=MibTableColumn
s5SbsViolationStatusMACAddress=_S5SbsViolationStatusMACAddress_Object((1,3,6,1,4,1,45,1,6,5,3,12,1,3),_S5SbsViolationStatusMACAddress_Type())
s5SbsViolationStatusMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsViolationStatusMACAddress.setStatus(_A)
class _S5SbsMgmViolationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmp',1),('web',2),('telnet',3)))
_S5SbsMgmViolationType_Type.__name__=_B
_S5SbsMgmViolationType_Object=MibScalar
s5SbsMgmViolationType=_S5SbsMgmViolationType_Object((1,3,6,1,4,1,45,1,6,5,3,13),_S5SbsMgmViolationType_Type())
s5SbsMgmViolationType.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsMgmViolationType.setStatus(_A)
_S5SbsMgmViolationIpAddress_Type=IpAddress
_S5SbsMgmViolationIpAddress_Object=MibScalar
s5SbsMgmViolationIpAddress=_S5SbsMgmViolationIpAddress_Object((1,3,6,1,4,1,45,1,6,5,3,14),_S5SbsMgmViolationIpAddress_Type())
s5SbsMgmViolationIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsMgmViolationIpAddress.setStatus(_A)
_S5SbsPortSecurityStatus_Type=PortSet
_S5SbsPortSecurityStatus_Object=MibScalar
s5SbsPortSecurityStatus=_S5SbsPortSecurityStatus_Object((1,3,6,1,4,1,45,1,6,5,3,15),_S5SbsPortSecurityStatus_Type())
s5SbsPortSecurityStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsPortSecurityStatus.setStatus(_A)
_S5SbsPortLearnStatus_Type=PortSet
_S5SbsPortLearnStatus_Object=MibScalar
s5SbsPortLearnStatus=_S5SbsPortLearnStatus_Object((1,3,6,1,4,1,45,1,6,5,3,16),_S5SbsPortLearnStatus_Type())
s5SbsPortLearnStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsPortLearnStatus.setStatus(_A)
class _S5SbsCurrSecurityLists_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsCurrSecurityLists_Type.__name__=_B
_S5SbsCurrSecurityLists_Object=MibScalar
s5SbsCurrSecurityLists=_S5SbsCurrSecurityLists_Object((1,3,6,1,4,1,45,1,6,5,3,17),_S5SbsCurrSecurityLists_Type())
s5SbsCurrSecurityLists.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsCurrSecurityLists.setStatus(_A)
class _S5SbsMaxSecurityLists_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsMaxSecurityLists_Type.__name__=_B
_S5SbsMaxSecurityLists_Object=MibScalar
s5SbsMaxSecurityLists=_S5SbsMaxSecurityLists_Object((1,3,6,1,4,1,45,1,6,5,3,18),_S5SbsMaxSecurityLists_Type())
s5SbsMaxSecurityLists.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsMaxSecurityLists.setStatus(_A)
_S5SbsSecurityListTable_Object=MibTable
s5SbsSecurityListTable=_S5SbsSecurityListTable_Object((1,3,6,1,4,1,45,1,6,5,3,19))
if mibBuilder.loadTexts:s5SbsSecurityListTable.setStatus(_A)
_S5SbsSecurityListEntry_Object=MibTableRow
s5SbsSecurityListEntry=_S5SbsSecurityListEntry_Object((1,3,6,1,4,1,45,1,6,5,3,19,1))
s5SbsSecurityListEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:s5SbsSecurityListEntry.setStatus(_A)
class _S5SbsSecurityListIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5SbsSecurityListIndx_Type.__name__=_B
_S5SbsSecurityListIndx_Object=MibTableColumn
s5SbsSecurityListIndx=_S5SbsSecurityListIndx_Object((1,3,6,1,4,1,45,1,6,5,3,19,1,1),_S5SbsSecurityListIndx_Type())
s5SbsSecurityListIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsSecurityListIndx.setStatus(_A)
_S5SbsSecurityListMembers_Type=PortSet
_S5SbsSecurityListMembers_Object=MibTableColumn
s5SbsSecurityListMembers=_S5SbsSecurityListMembers_Object((1,3,6,1,4,1,45,1,6,5,3,19,1,2),_S5SbsSecurityListMembers_Type())
s5SbsSecurityListMembers.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsSecurityListMembers.setStatus(_A)
class _S5SbsSecurityListStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_T,2),(_U,3),(_V,4)))
_S5SbsSecurityListStatus_Type.__name__=_B
_S5SbsSecurityListStatus_Object=MibTableColumn
s5SbsSecurityListStatus=_S5SbsSecurityListStatus_Object((1,3,6,1,4,1,45,1,6,5,3,19,1,3),_S5SbsSecurityListStatus_Type())
s5SbsSecurityListStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsSecurityListStatus.setStatus(_A)
_S5SbsMacViolation_ObjectIdentity=ObjectIdentity
s5SbsMacViolation=_S5SbsMacViolation_ObjectIdentity((1,3,6,1,4,1,45,1,6,5,3,20))
class _S5SbsMacViolationClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('clear',2)))
_S5SbsMacViolationClear_Type.__name__=_B
_S5SbsMacViolationClear_Object=MibScalar
s5SbsMacViolationClear=_S5SbsMacViolationClear_Object((1,3,6,1,4,1,45,1,6,5,3,20,1),_S5SbsMacViolationClear_Type())
s5SbsMacViolationClear.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsMacViolationClear.setStatus(_A)
_S5SbsMacViolationTable_Object=MibTable
s5SbsMacViolationTable=_S5SbsMacViolationTable_Object((1,3,6,1,4,1,45,1,6,5,3,20,2))
if mibBuilder.loadTexts:s5SbsMacViolationTable.setStatus(_A)
_S5SbsMacViolationEntry_Object=MibTableRow
s5SbsMacViolationEntry=_S5SbsMacViolationEntry_Object((1,3,6,1,4,1,45,1,6,5,3,20,2,1))
s5SbsMacViolationEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:s5SbsMacViolationEntry.setStatus(_A)
_S5SbsMacViolationAddress_Type=MacAddress
_S5SbsMacViolationAddress_Object=MibTableColumn
s5SbsMacViolationAddress=_S5SbsMacViolationAddress_Object((1,3,6,1,4,1,45,1,6,5,3,20,2,1,1),_S5SbsMacViolationAddress_Type())
s5SbsMacViolationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsMacViolationAddress.setStatus(_A)
class _S5SbsMacViolationBrd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsMacViolationBrd_Type.__name__=_B
_S5SbsMacViolationBrd_Object=MibTableColumn
s5SbsMacViolationBrd=_S5SbsMacViolationBrd_Object((1,3,6,1,4,1,45,1,6,5,3,20,2,1,2),_S5SbsMacViolationBrd_Type())
s5SbsMacViolationBrd.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsMacViolationBrd.setStatus(_A)
class _S5SbsMacViolationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsMacViolationPort_Type.__name__=_B
_S5SbsMacViolationPort_Object=MibTableColumn
s5SbsMacViolationPort=_S5SbsMacViolationPort_Object((1,3,6,1,4,1,45,1,6,5,3,20,2,1,3),_S5SbsMacViolationPort_Type())
s5SbsMacViolationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:s5SbsMacViolationPort.setStatus(_A)
class _S5SbsAutoLearningAgingTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsAutoLearningAgingTime_Type.__name__=_B
_S5SbsAutoLearningAgingTime_Object=MibScalar
s5SbsAutoLearningAgingTime=_S5SbsAutoLearningAgingTime_Object((1,3,6,1,4,1,45,1,6,5,3,21),_S5SbsAutoLearningAgingTime_Type())
s5SbsAutoLearningAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAutoLearningAgingTime.setStatus(_A)
if mibBuilder.loadTexts:s5SbsAutoLearningAgingTime.setUnits('Minutes')
_S5SbsAutoLearningConfigTable_Object=MibTable
s5SbsAutoLearningConfigTable=_S5SbsAutoLearningConfigTable_Object((1,3,6,1,4,1,45,1,6,5,3,22))
if mibBuilder.loadTexts:s5SbsAutoLearningConfigTable.setStatus(_A)
_S5SbsAutoLearningConfigEntry_Object=MibTableRow
s5SbsAutoLearningConfigEntry=_S5SbsAutoLearningConfigEntry_Object((1,3,6,1,4,1,45,1,6,5,3,22,1))
s5SbsAutoLearningConfigEntry.setIndexNames((0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:s5SbsAutoLearningConfigEntry.setStatus(_A)
class _S5SbsAutoLearningConfigBrd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsAutoLearningConfigBrd_Type.__name__=_B
_S5SbsAutoLearningConfigBrd_Object=MibTableColumn
s5SbsAutoLearningConfigBrd=_S5SbsAutoLearningConfigBrd_Object((1,3,6,1,4,1,45,1,6,5,3,22,1,1),_S5SbsAutoLearningConfigBrd_Type())
s5SbsAutoLearningConfigBrd.setMaxAccess(_G)
if mibBuilder.loadTexts:s5SbsAutoLearningConfigBrd.setStatus(_A)
class _S5SbsAutoLearningConfigPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5SbsAutoLearningConfigPort_Type.__name__=_B
_S5SbsAutoLearningConfigPort_Object=MibTableColumn
s5SbsAutoLearningConfigPort=_S5SbsAutoLearningConfigPort_Object((1,3,6,1,4,1,45,1,6,5,3,22,1,2),_S5SbsAutoLearningConfigPort_Type())
s5SbsAutoLearningConfigPort.setMaxAccess(_G)
if mibBuilder.loadTexts:s5SbsAutoLearningConfigPort.setStatus(_A)
class _S5SbsAutoLearningConfigEnabled_Type(TruthValue):defaultValue=2
_S5SbsAutoLearningConfigEnabled_Type.__name__=_H
_S5SbsAutoLearningConfigEnabled_Object=MibTableColumn
s5SbsAutoLearningConfigEnabled=_S5SbsAutoLearningConfigEnabled_Object((1,3,6,1,4,1,45,1,6,5,3,22,1,3),_S5SbsAutoLearningConfigEnabled_Type())
s5SbsAutoLearningConfigEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAutoLearningConfigEnabled.setStatus(_A)
class _S5SbsAutoLearningConfigMaxMacs_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_S5SbsAutoLearningConfigMaxMacs_Type.__name__=_B
_S5SbsAutoLearningConfigMaxMacs_Object=MibTableColumn
s5SbsAutoLearningConfigMaxMacs=_S5SbsAutoLearningConfigMaxMacs_Object((1,3,6,1,4,1,45,1,6,5,3,22,1,4),_S5SbsAutoLearningConfigMaxMacs_Type())
s5SbsAutoLearningConfigMaxMacs.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAutoLearningConfigMaxMacs.setStatus(_A)
_S5SbsAutoLearningPorts_Type=PortSet
_S5SbsAutoLearningPorts_Object=MibScalar
s5SbsAutoLearningPorts=_S5SbsAutoLearningPorts_Object((1,3,6,1,4,1,45,1,6,5,3,23),_S5SbsAutoLearningPorts_Type())
s5SbsAutoLearningPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAutoLearningPorts.setStatus(_A)
_S5SbsAutoLearningSticky_Type=TruthValue
_S5SbsAutoLearningSticky_Object=MibScalar
s5SbsAutoLearningSticky=_S5SbsAutoLearningSticky_Object((1,3,6,1,4,1,45,1,6,5,3,24),_S5SbsAutoLearningSticky_Type())
s5SbsAutoLearningSticky.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsAutoLearningSticky.setStatus(_A)
_S5SbsSecurityLockoutPortList_Type=PortSet
_S5SbsSecurityLockoutPortList_Object=MibScalar
s5SbsSecurityLockoutPortList=_S5SbsSecurityLockoutPortList_Object((1,3,6,1,4,1,45,1,6,5,3,25),_S5SbsSecurityLockoutPortList_Type())
s5SbsSecurityLockoutPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:s5SbsSecurityLockoutPortList.setStatus(_A)
_S5SbsDaFilteringTable_Object=MibTable
s5SbsDaFilteringTable=_S5SbsDaFilteringTable_Object((1,3,6,1,4,1,45,1,6,5,3,26))
if mibBuilder.loadTexts:s5SbsDaFilteringTable.setStatus(_A)
_S5SbsDaFilteringEntry_Object=MibTableRow
s5SbsDaFilteringEntry=_S5SbsDaFilteringEntry_Object((1,3,6,1,4,1,45,1,6,5,3,26,1))
s5SbsDaFilteringEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:s5SbsDaFilteringEntry.setStatus(_A)
class _S5SbsDaFilteringIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_S5SbsDaFilteringIndx_Type.__name__=_B
_S5SbsDaFilteringIndx_Object=MibTableColumn
s5SbsDaFilteringIndx=_S5SbsDaFilteringIndx_Object((1,3,6,1,4,1,45,1,6,5,3,26,1,1),_S5SbsDaFilteringIndx_Type())
s5SbsDaFilteringIndx.setMaxAccess(_G)
if mibBuilder.loadTexts:s5SbsDaFilteringIndx.setStatus(_A)
_S5SbsDaFilteringAddress_Type=MacAddress
_S5SbsDaFilteringAddress_Object=MibTableColumn
s5SbsDaFilteringAddress=_S5SbsDaFilteringAddress_Object((1,3,6,1,4,1,45,1,6,5,3,26,1,2),_S5SbsDaFilteringAddress_Type())
s5SbsDaFilteringAddress.setMaxAccess(_g)
if mibBuilder.loadTexts:s5SbsDaFilteringAddress.setStatus(_A)
class _S5SbsDaFilteringStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('add',2),('remove',3)))
_S5SbsDaFilteringStatus_Type.__name__=_B
_S5SbsDaFilteringStatus_Object=MibTableColumn
s5SbsDaFilteringStatus=_S5SbsDaFilteringStatus_Object((1,3,6,1,4,1,45,1,6,5,3,26,1,3),_S5SbsDaFilteringStatus_Type())
s5SbsDaFilteringStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:s5SbsDaFilteringStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PortSet':PortSet,'s5SbsAuth':s5SbsAuth,'s5SbsAuthSecurityLock':s5SbsAuthSecurityLock,'s5SbsAuthCtlPartTime':s5SbsAuthCtlPartTime,'s5SbsSecurityStatus':s5SbsSecurityStatus,'s5SbsSecurityMode':s5SbsSecurityMode,'s5SbsSecurityAction':s5SbsSecurityAction,'s5SbsCurrNodesAllowed':s5SbsCurrNodesAllowed,'s5SbsMaxNodesAllowed':s5SbsMaxNodesAllowed,'s5SbsCurrNodesBlocked':s5SbsCurrNodesBlocked,'s5SbsMaxNodesBlocked':s5SbsMaxNodesBlocked,'s5SbsAuthCfgTable':s5SbsAuthCfgTable,'s5SbsAuthCfgEntry':s5SbsAuthCfgEntry,_Q:s5SbsAuthCfgBrdIndx,_R:s5SbsAuthCfgPortIndx,_S:s5SbsAuthCfgMACIndx,'s5SbsAuthCfgAccessCtrlType':s5SbsAuthCfgAccessCtrlType,'s5SbsAuthCfgStatus':s5SbsAuthCfgStatus,'s5SbsAuthCfgSecureList':s5SbsAuthCfgSecureList,'s5SbsAuthCfgSource':s5SbsAuthCfgSource,'s5SbsAuthCfgLifetime':s5SbsAuthCfgLifetime,'s5SbsAuthCfgTrunk':s5SbsAuthCfgTrunk,'s5SbsAuthStatusTable':s5SbsAuthStatusTable,'s5SbsAuthStatusEntry':s5SbsAuthStatusEntry,_W:s5SbsAuthStatusBrdIndx,_X:s5SbsAuthStatusPortIndx,_Y:s5SbsAuthStatusMACIndx,'s5SbsCurrentAccessCtrlType':s5SbsCurrentAccessCtrlType,'s5SbsCurrentActionMode':s5SbsCurrentActionMode,'s5SbsCurrentPortSecurStatus':s5SbsCurrentPortSecurStatus,'s5SbsViolationStatusTable':s5SbsViolationStatusTable,'s5SbsViolationStatusEntry':s5SbsViolationStatusEntry,_Z:s5SbsViolationStatusBrdIndx,_a:s5SbsViolationStatusPortIndx,'s5SbsViolationStatusMACAddress':s5SbsViolationStatusMACAddress,'s5SbsMgmViolationType':s5SbsMgmViolationType,'s5SbsMgmViolationIpAddress':s5SbsMgmViolationIpAddress,'s5SbsPortSecurityStatus':s5SbsPortSecurityStatus,'s5SbsPortLearnStatus':s5SbsPortLearnStatus,'s5SbsCurrSecurityLists':s5SbsCurrSecurityLists,'s5SbsMaxSecurityLists':s5SbsMaxSecurityLists,'s5SbsSecurityListTable':s5SbsSecurityListTable,'s5SbsSecurityListEntry':s5SbsSecurityListEntry,_b:s5SbsSecurityListIndx,'s5SbsSecurityListMembers':s5SbsSecurityListMembers,'s5SbsSecurityListStatus':s5SbsSecurityListStatus,'s5SbsMacViolation':s5SbsMacViolation,'s5SbsMacViolationClear':s5SbsMacViolationClear,'s5SbsMacViolationTable':s5SbsMacViolationTable,'s5SbsMacViolationEntry':s5SbsMacViolationEntry,_c:s5SbsMacViolationAddress,'s5SbsMacViolationBrd':s5SbsMacViolationBrd,'s5SbsMacViolationPort':s5SbsMacViolationPort,'s5SbsAutoLearningAgingTime':s5SbsAutoLearningAgingTime,'s5SbsAutoLearningConfigTable':s5SbsAutoLearningConfigTable,'s5SbsAutoLearningConfigEntry':s5SbsAutoLearningConfigEntry,_d:s5SbsAutoLearningConfigBrd,_e:s5SbsAutoLearningConfigPort,'s5SbsAutoLearningConfigEnabled':s5SbsAutoLearningConfigEnabled,'s5SbsAutoLearningConfigMaxMacs':s5SbsAutoLearningConfigMaxMacs,'s5SbsAutoLearningPorts':s5SbsAutoLearningPorts,'s5SbsAutoLearningSticky':s5SbsAutoLearningSticky,'s5SbsSecurityLockoutPortList':s5SbsSecurityLockoutPortList,'s5SbsDaFilteringTable':s5SbsDaFilteringTable,'s5SbsDaFilteringEntry':s5SbsDaFilteringEntry,_f:s5SbsDaFilteringIndx,'s5SbsDaFilteringAddress':s5SbsDaFilteringAddress,'s5SbsDaFilteringStatus':s5SbsDaFilteringStatus})