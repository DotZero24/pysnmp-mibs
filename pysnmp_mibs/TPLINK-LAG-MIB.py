_L='passive'
_K='active'
_J='tpLagIndex'
_I='TPLINK-LAG-MIB'
_H='ifIndex'
_G='IF-MIB'
_F='read-create'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkLagMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,9))
if mibBuilder.loadTexts:tplinkLagMIB.setRevisions(('2012-12-13 09:30',))
_TplinkLagMIBObjects_ObjectIdentity=ObjectIdentity
tplinkLagMIBObjects=_TplinkLagMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,9,1))
_TplinkLagMIBGlobalConfig_ObjectIdentity=ObjectIdentity
tplinkLagMIBGlobalConfig=_TplinkLagMIBGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,9,1,1))
_TpLagMaxEntryNum_Type=Integer32
_TpLagMaxEntryNum_Object=MibScalar
tpLagMaxEntryNum=_TpLagMaxEntryNum_Object((1,3,6,1,4,1,11863,6,9,1,1,1),_TpLagMaxEntryNum_Type())
tpLagMaxEntryNum.setMaxAccess(_D)
if mibBuilder.loadTexts:tpLagMaxEntryNum.setStatus(_A)
class _TpLagLoadBalance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('mac-source',0),('mac-dest',1),('mac-source-dest',2),('ip-source',3),('ip-dest',4),('ip-source-dest',5)))
_TpLagLoadBalance_Type.__name__=_B
_TpLagLoadBalance_Object=MibScalar
tpLagLoadBalance=_TpLagLoadBalance_Object((1,3,6,1,4,1,11863,6,9,1,1,2),_TpLagLoadBalance_Type())
tpLagLoadBalance.setMaxAccess(_C)
if mibBuilder.loadTexts:tpLagLoadBalance.setStatus(_A)
_TplinkLagTable_ObjectIdentity=ObjectIdentity
tplinkLagTable=_TplinkLagTable_ObjectIdentity((1,3,6,1,4,1,11863,6,9,1,2))
_TpLagTable_Object=MibTable
tpLagTable=_TpLagTable_Object((1,3,6,1,4,1,11863,6,9,1,2,3))
if mibBuilder.loadTexts:tpLagTable.setStatus(_A)
_TpLagEntry_Object=MibTableRow
tpLagEntry=_TpLagEntry_Object((1,3,6,1,4,1,11863,6,9,1,2,3,1))
tpLagEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:tpLagEntry.setStatus(_A)
_TpLagIndex_Type=Integer32
_TpLagIndex_Object=MibTableColumn
tpLagIndex=_TpLagIndex_Object((1,3,6,1,4,1,11863,6,9,1,2,3,1,1),_TpLagIndex_Type())
tpLagIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpLagIndex.setStatus(_A)
class _TpLagType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),(_K,2),(_L,3)))
_TpLagType_Type.__name__=_B
_TpLagType_Object=MibTableColumn
tpLagType=_TpLagType_Object((1,3,6,1,4,1,11863,6,9,1,2,3,1,2),_TpLagType_Type())
tpLagType.setMaxAccess(_F)
if mibBuilder.loadTexts:tpLagType.setStatus(_A)
class _TpLagMember_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_TpLagMember_Type.__name__=_E
_TpLagMember_Object=MibTableColumn
tpLagMember=_TpLagMember_Object((1,3,6,1,4,1,11863,6,9,1,2,3,1,3),_TpLagMember_Type())
tpLagMember.setMaxAccess(_F)
if mibBuilder.loadTexts:tpLagMember.setStatus(_A)
_TpLagRowStatus_Type=RowStatus
_TpLagRowStatus_Object=MibTableColumn
tpLagRowStatus=_TpLagRowStatus_Object((1,3,6,1,4,1,11863,6,9,1,2,3,1,4),_TpLagRowStatus_Type())
tpLagRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:tpLagRowStatus.setStatus(_A)
_TplinkLagLacpManage_ObjectIdentity=ObjectIdentity
tplinkLagLacpManage=_TplinkLagLacpManage_ObjectIdentity((1,3,6,1,4,1,11863,6,9,1,3))
class _TpLacpSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TpLacpSystemPriority_Type.__name__=_B
_TpLacpSystemPriority_Object=MibScalar
tpLacpSystemPriority=_TpLacpSystemPriority_Object((1,3,6,1,4,1,11863,6,9,1,3,1),_TpLacpSystemPriority_Type())
tpLacpSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:tpLacpSystemPriority.setStatus(_A)
_TpLacpTable_Object=MibTable
tpLacpTable=_TpLacpTable_Object((1,3,6,1,4,1,11863,6,9,1,3,2))
if mibBuilder.loadTexts:tpLacpTable.setStatus(_A)
_TpLacpEntry_Object=MibTableRow
tpLacpEntry=_TpLacpEntry_Object((1,3,6,1,4,1,11863,6,9,1,3,2,1))
tpLacpEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tpLacpEntry.setStatus(_A)
_TpLacpPort_Type=DisplayString
_TpLacpPort_Object=MibTableColumn
tpLacpPort=_TpLacpPort_Object((1,3,6,1,4,1,11863,6,9,1,3,2,1,1),_TpLacpPort_Type())
tpLacpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tpLacpPort.setStatus(_A)
class _TpLacpAdminKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TpLacpAdminKey_Type.__name__=_B
_TpLacpAdminKey_Object=MibTableColumn
tpLacpAdminKey=_TpLacpAdminKey_Object((1,3,6,1,4,1,11863,6,9,1,3,2,1,2),_TpLacpAdminKey_Type())
tpLacpAdminKey.setMaxAccess(_C)
if mibBuilder.loadTexts:tpLacpAdminKey.setStatus(_A)
class _TpLacpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TpLacpPortPriority_Type.__name__=_B
_TpLacpPortPriority_Object=MibTableColumn
tpLacpPortPriority=_TpLacpPortPriority_Object((1,3,6,1,4,1,11863,6,9,1,3,2,1,3),_TpLacpPortPriority_Type())
tpLacpPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:tpLacpPortPriority.setStatus(_A)
class _TpLacpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_K,1)))
_TpLacpMode_Type.__name__=_B
_TpLacpMode_Object=MibTableColumn
tpLacpMode=_TpLacpMode_Object((1,3,6,1,4,1,11863,6,9,1,3,2,1,4),_TpLacpMode_Type())
tpLacpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tpLacpMode.setStatus(_A)
class _TpLacpChan_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TpLacpChan_Type.__name__=_E
_TpLacpChan_Object=MibTableColumn
tpLacpChan=_TpLacpChan_Object((1,3,6,1,4,1,11863,6,9,1,3,2,1,5),_TpLacpChan_Type())
tpLacpChan.setMaxAccess(_D)
if mibBuilder.loadTexts:tpLacpChan.setStatus(_A)
_TplinkLagNotifications_ObjectIdentity=ObjectIdentity
tplinkLagNotifications=_TplinkLagNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,9,2))
mibBuilder.exportSymbols(_I,**{'tplinkLagMIB':tplinkLagMIB,'tplinkLagMIBObjects':tplinkLagMIBObjects,'tplinkLagMIBGlobalConfig':tplinkLagMIBGlobalConfig,'tpLagMaxEntryNum':tpLagMaxEntryNum,'tpLagLoadBalance':tpLagLoadBalance,'tplinkLagTable':tplinkLagTable,'tpLagTable':tpLagTable,'tpLagEntry':tpLagEntry,_J:tpLagIndex,'tpLagType':tpLagType,'tpLagMember':tpLagMember,'tpLagRowStatus':tpLagRowStatus,'tplinkLagLacpManage':tplinkLagLacpManage,'tpLacpSystemPriority':tpLacpSystemPriority,'tpLacpTable':tpLacpTable,'tpLacpEntry':tpLacpEntry,'tpLacpPort':tpLacpPort,'tpLacpAdminKey':tpLacpAdminKey,'tpLacpPortPriority':tpLacpPortPriority,'tpLacpMode':tpLacpMode,'tpLacpChan':tpLacpChan,'tplinkLagNotifications':tplinkLagNotifications})