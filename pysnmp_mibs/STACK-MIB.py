_G='zxr10StkDeviceID'
_F='sysStkDeviceID'
_E='STACK-MIB'
_D='DisplayString'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
stack=ModuleIdentity((1,3,6,1,4,1,3902,3,300))
if mibBuilder.loadTexts:stack.setRevisions(('2004-05-14 00:00',))
class MasterSlaveDataSynStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(11,12,13,20,40,50,60,70,80,90,100)));namedValues=NamedValues(*(('masterinit',11),('backinit',12),('memberinit',13),('masteridle',20),('backreg',40),('interaction',50),('masterbatchsync',60),('backbatchsync',70),('masterrealsync',80),('backrealsync',90),('mastergr',100)))
class StkDeviceStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('master',0),('slave',1),('member',2)))
class VendorIdType(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_SystemGrp_ObjectIdentity=ObjectIdentity
systemGrp=_SystemGrp_ObjectIdentity((1,3,6,1,4,1,3902,3,300,1))
_SysNetMask_Type=IpAddress
_SysNetMask_Object=MibScalar
sysNetMask=_SysNetMask_Object((1,3,6,1,4,1,3902,3,300,1,1),_SysNetMask_Type())
sysNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:sysNetMask.setStatus('deprecated')
class _SysManagIf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysManagIf_Type.__name__=_D
_SysManagIf_Object=MibScalar
sysManagIf=_SysManagIf_Object((1,3,6,1,4,1,3902,3,300,1,2),_SysManagIf_Type())
sysManagIf.setMaxAccess(_C)
if mibBuilder.loadTexts:sysManagIf.setStatus(_A)
_SysMacAddr_Type=MacAddress
_SysMacAddr_Object=MibScalar
sysMacAddr=_SysMacAddr_Object((1,3,6,1,4,1,3902,3,300,1,3),_SysMacAddr_Type())
sysMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMacAddr.setStatus(_A)
_SysMacChagAgingTime_Type=Integer32
_SysMacChagAgingTime_Object=MibScalar
sysMacChagAgingTime=_SysMacChagAgingTime_Object((1,3,6,1,4,1,3902,3,300,1,4),_SysMacChagAgingTime_Type())
sysMacChagAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMacChagAgingTime.setStatus(_A)
class _SysLastchagConfigTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SysLastchagConfigTime_Type.__name__=_D
_SysLastchagConfigTime_Object=MibScalar
sysLastchagConfigTime=_SysLastchagConfigTime_Object((1,3,6,1,4,1,3902,3,300,1,5),_SysLastchagConfigTime_Type())
sysLastchagConfigTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysLastchagConfigTime.setStatus(_A)
_SysMasterSlaveDataSynStatus_Type=MasterSlaveDataSynStatus
_SysMasterSlaveDataSynStatus_Object=MibScalar
sysMasterSlaveDataSynStatus=_SysMasterSlaveDataSynStatus_Object((1,3,6,1,4,1,3902,3,300,1,6),_SysMasterSlaveDataSynStatus_Type())
sysMasterSlaveDataSynStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysMasterSlaveDataSynStatus.setStatus(_A)
_SysManagIpAddr_Type=IpAddress
_SysManagIpAddr_Object=MibScalar
sysManagIpAddr=_SysManagIpAddr_Object((1,3,6,1,4,1,3902,3,300,1,7),_SysManagIpAddr_Type())
sysManagIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sysManagIpAddr.setStatus(_A)
_SysStkDeviceInfoTable_Object=MibTable
sysStkDeviceInfoTable=_SysStkDeviceInfoTable_Object((1,3,6,1,4,1,3902,3,300,2))
if mibBuilder.loadTexts:sysStkDeviceInfoTable.setStatus(_A)
_SysStkDeviceInfoEntry_Object=MibTableRow
sysStkDeviceInfoEntry=_SysStkDeviceInfoEntry_Object((1,3,6,1,4,1,3902,3,300,2,1))
sysStkDeviceInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sysStkDeviceInfoEntry.setStatus(_A)
_SysStkDeviceID_Type=Integer32
_SysStkDeviceID_Object=MibTableColumn
sysStkDeviceID=_SysStkDeviceID_Object((1,3,6,1,4,1,3902,3,300,2,1,1),_SysStkDeviceID_Type())
sysStkDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:sysStkDeviceID.setStatus(_A)
_SysStkDeviceType_Type=Integer32
_SysStkDeviceType_Object=MibTableColumn
sysStkDeviceType=_SysStkDeviceType_Object((1,3,6,1,4,1,3902,3,300,2,1,2),_SysStkDeviceType_Type())
sysStkDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:sysStkDeviceType.setStatus(_A)
_SysMemDeviceMacAddr_Type=MacAddress
_SysMemDeviceMacAddr_Object=MibTableColumn
sysMemDeviceMacAddr=_SysMemDeviceMacAddr_Object((1,3,6,1,4,1,3902,3,300,2,1,3),_SysMemDeviceMacAddr_Type())
sysMemDeviceMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sysMemDeviceMacAddr.setStatus(_A)
_SysMemUpTime_Type=TimeTicks
_SysMemUpTime_Object=MibTableColumn
sysMemUpTime=_SysMemUpTime_Object((1,3,6,1,4,1,3902,3,300,2,1,4),_SysMemUpTime_Type())
sysMemUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysMemUpTime.setStatus(_A)
_SysStkDeviceStatus_Type=StkDeviceStatus
_SysStkDeviceStatus_Object=MibTableColumn
sysStkDeviceStatus=_SysStkDeviceStatus_Object((1,3,6,1,4,1,3902,3,300,2,1,5),_SysStkDeviceStatus_Type())
sysStkDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysStkDeviceStatus.setStatus(_A)
_Zxr10StackStatTable_Object=MibTable
zxr10StackStatTable=_Zxr10StackStatTable_Object((1,3,6,1,4,1,3902,3,300,3))
if mibBuilder.loadTexts:zxr10StackStatTable.setStatus(_A)
_Zxr10StackStatEntry_Object=MibTableRow
zxr10StackStatEntry=_Zxr10StackStatEntry_Object((1,3,6,1,4,1,3902,3,300,3,1))
zxr10StackStatEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:zxr10StackStatEntry.setStatus(_A)
_Zxr10StkDeviceID_Type=Integer32
_Zxr10StkDeviceID_Object=MibTableColumn
zxr10StkDeviceID=_Zxr10StkDeviceID_Object((1,3,6,1,4,1,3902,3,300,3,1,1),_Zxr10StkDeviceID_Type())
zxr10StkDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10StkDeviceID.setStatus(_A)
_Zxr10StkDeviceMacAddr_Type=MacAddress
_Zxr10StkDeviceMacAddr_Object=MibTableColumn
zxr10StkDeviceMacAddr=_Zxr10StkDeviceMacAddr_Object((1,3,6,1,4,1,3902,3,300,3,1,2),_Zxr10StkDeviceMacAddr_Type())
zxr10StkDeviceMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10StkDeviceMacAddr.setStatus(_A)
_Zxr10StkDeviceCpuUtility5s_Type=DisplayString
_Zxr10StkDeviceCpuUtility5s_Object=MibTableColumn
zxr10StkDeviceCpuUtility5s=_Zxr10StkDeviceCpuUtility5s_Object((1,3,6,1,4,1,3902,3,300,3,1,3),_Zxr10StkDeviceCpuUtility5s_Type())
zxr10StkDeviceCpuUtility5s.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10StkDeviceCpuUtility5s.setStatus(_A)
_Zxr10StkDeviceCpuUtility1m_Type=DisplayString
_Zxr10StkDeviceCpuUtility1m_Object=MibTableColumn
zxr10StkDeviceCpuUtility1m=_Zxr10StkDeviceCpuUtility1m_Object((1,3,6,1,4,1,3902,3,300,3,1,4),_Zxr10StkDeviceCpuUtility1m_Type())
zxr10StkDeviceCpuUtility1m.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10StkDeviceCpuUtility1m.setStatus(_A)
_Zxr10StkDeviceCpuUtility5m_Type=DisplayString
_Zxr10StkDeviceCpuUtility5m_Object=MibTableColumn
zxr10StkDeviceCpuUtility5m=_Zxr10StkDeviceCpuUtility5m_Object((1,3,6,1,4,1,3902,3,300,3,1,5),_Zxr10StkDeviceCpuUtility5m_Type())
zxr10StkDeviceCpuUtility5m.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10StkDeviceCpuUtility5m.setStatus(_A)
_Zxr10StkDeviceMemUtility_Type=DisplayString
_Zxr10StkDeviceMemUtility_Object=MibTableColumn
zxr10StkDeviceMemUtility=_Zxr10StkDeviceMemUtility_Object((1,3,6,1,4,1,3902,3,300,3,1,6),_Zxr10StkDeviceMemUtility_Type())
zxr10StkDeviceMemUtility.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10StkDeviceMemUtility.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MasterSlaveDataSynStatus':MasterSlaveDataSynStatus,'StkDeviceStatus':StkDeviceStatus,'VendorIdType':VendorIdType,'zte':zte,'zxr10':zxr10,'stack':stack,'systemGrp':systemGrp,'sysNetMask':sysNetMask,'sysManagIf':sysManagIf,'sysMacAddr':sysMacAddr,'sysMacChagAgingTime':sysMacChagAgingTime,'sysLastchagConfigTime':sysLastchagConfigTime,'sysMasterSlaveDataSynStatus':sysMasterSlaveDataSynStatus,'sysManagIpAddr':sysManagIpAddr,'sysStkDeviceInfoTable':sysStkDeviceInfoTable,'sysStkDeviceInfoEntry':sysStkDeviceInfoEntry,_F:sysStkDeviceID,'sysStkDeviceType':sysStkDeviceType,'sysMemDeviceMacAddr':sysMemDeviceMacAddr,'sysMemUpTime':sysMemUpTime,'sysStkDeviceStatus':sysStkDeviceStatus,'zxr10StackStatTable':zxr10StackStatTable,'zxr10StackStatEntry':zxr10StackStatEntry,_G:zxr10StkDeviceID,'zxr10StkDeviceMacAddr':zxr10StkDeviceMacAddr,'zxr10StkDeviceCpuUtility5s':zxr10StkDeviceCpuUtility5s,'zxr10StkDeviceCpuUtility1m':zxr10StkDeviceCpuUtility1m,'zxr10StkDeviceCpuUtility5m':zxr10StkDeviceCpuUtility5m,'zxr10StkDeviceMemUtility':zxr10StkDeviceMemUtility})