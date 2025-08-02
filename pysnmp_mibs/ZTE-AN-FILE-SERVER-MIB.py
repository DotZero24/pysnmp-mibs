_R='zxAnFileServerGroup'
_Q='zxAnFileServerGroupGroup'
_P='zxAnFileServerPath'
_O='zxAnFileServerUserPwd'
_N='zxAnFileServerUserName'
_M='zxAnFileServerProtocolType'
_L='zxAnFileServerIpAddress'
_K='zxAnFileServerIpAddressType'
_J='zxAnFileServerGroupWorkMode'
_I='zxAnFileServerIndex'
_H='not-accessible'
_G='InetAddressType'
_F='zxAnFileServerGroupUsage'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='ZTE-AN-FILE-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnFileServerMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,17))
if mibBuilder.loadTexts:zxAnFileServerMib.setRevisions(('2011-05-26 00:00',))
_ZxAnFileServerObjects_ObjectIdentity=ObjectIdentity
zxAnFileServerObjects=_ZxAnFileServerObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,17,2))
_ZxAnFileServerGroupTable_Object=MibTable
zxAnFileServerGroupTable=_ZxAnFileServerGroupTable_Object((1,3,6,1,4,1,3902,1015,17,2,2))
if mibBuilder.loadTexts:zxAnFileServerGroupTable.setStatus(_A)
_ZxAnFileServerGroupEntry_Object=MibTableRow
zxAnFileServerGroupEntry=_ZxAnFileServerGroupEntry_Object((1,3,6,1,4,1,3902,1015,17,2,2,1))
zxAnFileServerGroupEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxAnFileServerGroupEntry.setStatus(_A)
class _ZxAnFileServerGroupUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,31)));namedValues=NamedValues(*(('autoBackupConfiguration',1),('manualBackupConfiguration',2),('autoBackupLog',3),('manualBackupLog',4),('autoBackupSoftware',5),('manualBackupSoftware',6),('downloadPerformance',7),('uploadPerformance',8),('autoUpdateSoftware',31)))
_ZxAnFileServerGroupUsage_Type.__name__=_D
_ZxAnFileServerGroupUsage_Object=MibTableColumn
zxAnFileServerGroupUsage=_ZxAnFileServerGroupUsage_Object((1,3,6,1,4,1,3902,1015,17,2,2,1,1),_ZxAnFileServerGroupUsage_Type())
zxAnFileServerGroupUsage.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnFileServerGroupUsage.setStatus(_A)
class _ZxAnFileServerGroupWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('roundRobin',1))
_ZxAnFileServerGroupWorkMode_Type.__name__=_D
_ZxAnFileServerGroupWorkMode_Object=MibTableColumn
zxAnFileServerGroupWorkMode=_ZxAnFileServerGroupWorkMode_Object((1,3,6,1,4,1,3902,1015,17,2,2,1,2),_ZxAnFileServerGroupWorkMode_Type())
zxAnFileServerGroupWorkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnFileServerGroupWorkMode.setStatus(_A)
_ZxAnFileServerTable_Object=MibTable
zxAnFileServerTable=_ZxAnFileServerTable_Object((1,3,6,1,4,1,3902,1015,17,2,3))
if mibBuilder.loadTexts:zxAnFileServerTable.setStatus(_A)
_ZxAnFileServerEntry_Object=MibTableRow
zxAnFileServerEntry=_ZxAnFileServerEntry_Object((1,3,6,1,4,1,3902,1015,17,2,3,1))
zxAnFileServerEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxAnFileServerEntry.setStatus(_A)
class _ZxAnFileServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ZxAnFileServerIndex_Type.__name__=_D
_ZxAnFileServerIndex_Object=MibTableColumn
zxAnFileServerIndex=_ZxAnFileServerIndex_Object((1,3,6,1,4,1,3902,1015,17,2,3,1,1),_ZxAnFileServerIndex_Type())
zxAnFileServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnFileServerIndex.setStatus(_A)
class _ZxAnFileServerIpAddressType_Type(InetAddressType):defaultValue=1
_ZxAnFileServerIpAddressType_Type.__name__=_G
_ZxAnFileServerIpAddressType_Object=MibTableColumn
zxAnFileServerIpAddressType=_ZxAnFileServerIpAddressType_Object((1,3,6,1,4,1,3902,1015,17,2,3,1,2),_ZxAnFileServerIpAddressType_Type())
zxAnFileServerIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnFileServerIpAddressType.setStatus(_A)
_ZxAnFileServerIpAddress_Type=InetAddress
_ZxAnFileServerIpAddress_Object=MibTableColumn
zxAnFileServerIpAddress=_ZxAnFileServerIpAddress_Object((1,3,6,1,4,1,3902,1015,17,2,3,1,3),_ZxAnFileServerIpAddress_Type())
zxAnFileServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnFileServerIpAddress.setStatus(_A)
class _ZxAnFileServerProtocolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ftp',1),('sftp',2),('none',3)))
_ZxAnFileServerProtocolType_Type.__name__=_D
_ZxAnFileServerProtocolType_Object=MibTableColumn
zxAnFileServerProtocolType=_ZxAnFileServerProtocolType_Object((1,3,6,1,4,1,3902,1015,17,2,3,1,4),_ZxAnFileServerProtocolType_Type())
zxAnFileServerProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnFileServerProtocolType.setStatus(_A)
class _ZxAnFileServerUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnFileServerUserName_Type.__name__=_E
_ZxAnFileServerUserName_Object=MibTableColumn
zxAnFileServerUserName=_ZxAnFileServerUserName_Object((1,3,6,1,4,1,3902,1015,17,2,3,1,5),_ZxAnFileServerUserName_Type())
zxAnFileServerUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnFileServerUserName.setStatus(_A)
class _ZxAnFileServerUserPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnFileServerUserPwd_Type.__name__=_E
_ZxAnFileServerUserPwd_Object=MibTableColumn
zxAnFileServerUserPwd=_ZxAnFileServerUserPwd_Object((1,3,6,1,4,1,3902,1015,17,2,3,1,6),_ZxAnFileServerUserPwd_Type())
zxAnFileServerUserPwd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnFileServerUserPwd.setStatus(_A)
class _ZxAnFileServerPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxAnFileServerPath_Type.__name__=_E
_ZxAnFileServerPath_Object=MibTableColumn
zxAnFileServerPath=_ZxAnFileServerPath_Object((1,3,6,1,4,1,3902,1015,17,2,3,1,7),_ZxAnFileServerPath_Type())
zxAnFileServerPath.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnFileServerPath.setStatus(_A)
_ZxAnFileServerConformance_ObjectIdentity=ObjectIdentity
zxAnFileServerConformance=_ZxAnFileServerConformance_ObjectIdentity((1,3,6,1,4,1,3902,1015,17,4))
_ZxAnFileServerCompliances_ObjectIdentity=ObjectIdentity
zxAnFileServerCompliances=_ZxAnFileServerCompliances_ObjectIdentity((1,3,6,1,4,1,3902,1015,17,4,1))
_ZxAnFileServerGroups_ObjectIdentity=ObjectIdentity
zxAnFileServerGroups=_ZxAnFileServerGroups_ObjectIdentity((1,3,6,1,4,1,3902,1015,17,4,2))
zxAnFileServerGroupGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,17,4,2,1))
zxAnFileServerGroupGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:zxAnFileServerGroupGroup.setStatus(_A)
zxAnFileServerGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,17,4,2,2))
zxAnFileServerGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:zxAnFileServerGroup.setStatus(_A)
zxAnFileServerCompliance=ModuleCompliance((1,3,6,1,4,1,3902,1015,17,4,1,1))
zxAnFileServerCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:zxAnFileServerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnFileServerMib':zxAnFileServerMib,'zxAnFileServerObjects':zxAnFileServerObjects,'zxAnFileServerGroupTable':zxAnFileServerGroupTable,'zxAnFileServerGroupEntry':zxAnFileServerGroupEntry,_F:zxAnFileServerGroupUsage,_J:zxAnFileServerGroupWorkMode,'zxAnFileServerTable':zxAnFileServerTable,'zxAnFileServerEntry':zxAnFileServerEntry,_I:zxAnFileServerIndex,_K:zxAnFileServerIpAddressType,_L:zxAnFileServerIpAddress,_M:zxAnFileServerProtocolType,_N:zxAnFileServerUserName,_O:zxAnFileServerUserPwd,_P:zxAnFileServerPath,'zxAnFileServerConformance':zxAnFileServerConformance,'zxAnFileServerCompliances':zxAnFileServerCompliances,'zxAnFileServerCompliance':zxAnFileServerCompliance,'zxAnFileServerGroups':zxAnFileServerGroups,_Q:zxAnFileServerGroupGroup,_R:zxAnFileServerGroup})