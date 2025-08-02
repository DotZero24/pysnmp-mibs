_J='zxAnVmacIfTranslateSrcMac'
_I='zxAnVmacIfTranslateVid'
_H='read-write'
_G='zxAnVmacVid'
_F='zxAnVmacIfIndex'
_E='read-create'
_D='not-accessible'
_C='Integer32'
_B='ZTE-AN-VMAC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
VlanId,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','VlanId','zxAn')
zxAnVmacMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,101))
if mibBuilder.loadTexts:zxAnVmacMib.setRevisions(('1913-08-16 00:00',))
_ZxAnVmacObjects_ObjectIdentity=ObjectIdentity
zxAnVmacObjects=_ZxAnVmacObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,101,2))
_ZxAnVmacVlanObjects_ObjectIdentity=ObjectIdentity
zxAnVmacVlanObjects=_ZxAnVmacVlanObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,101,2,1))
_ZxAnVmacVlanTable_Object=MibTable
zxAnVmacVlanTable=_ZxAnVmacVlanTable_Object((1,3,6,1,4,1,3902,1015,101,2,1,2))
if mibBuilder.loadTexts:zxAnVmacVlanTable.setStatus(_A)
_ZxAnVmacVlanEntry_Object=MibTableRow
zxAnVmacVlanEntry=_ZxAnVmacVlanEntry_Object((1,3,6,1,4,1,3902,1015,101,2,1,2,1))
zxAnVmacVlanEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:zxAnVmacVlanEntry.setStatus(_A)
_ZxAnVmacVid_Type=VlanId
_ZxAnVmacVid_Object=MibTableColumn
zxAnVmacVid=_ZxAnVmacVid_Object((1,3,6,1,4,1,3902,1015,101,2,1,2,1,1),_ZxAnVmacVid_Type())
zxAnVmacVid.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVmacVid.setStatus(_A)
class _ZxAnVmacMacPoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnVmacMacPoolIndex_Type.__name__=_C
_ZxAnVmacMacPoolIndex_Object=MibTableColumn
zxAnVmacMacPoolIndex=_ZxAnVmacMacPoolIndex_Object((1,3,6,1,4,1,3902,1015,101,2,1,2,1,2),_ZxAnVmacMacPoolIndex_Type())
zxAnVmacMacPoolIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVmacMacPoolIndex.setStatus(_A)
_ZxAnVmacVlanRowStatus_Type=RowStatus
_ZxAnVmacVlanRowStatus_Object=MibTableColumn
zxAnVmacVlanRowStatus=_ZxAnVmacVlanRowStatus_Object((1,3,6,1,4,1,3902,1015,101,2,1,2,1,50),_ZxAnVmacVlanRowStatus_Type())
zxAnVmacVlanRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVmacVlanRowStatus.setStatus(_A)
_ZxAnVmacIfObjects_ObjectIdentity=ObjectIdentity
zxAnVmacIfObjects=_ZxAnVmacIfObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,101,2,2))
_ZxAnVmacIfConfTable_Object=MibTable
zxAnVmacIfConfTable=_ZxAnVmacIfConfTable_Object((1,3,6,1,4,1,3902,1015,101,2,2,2))
if mibBuilder.loadTexts:zxAnVmacIfConfTable.setStatus(_A)
_ZxAnVmacIfConfEntry_Object=MibTableRow
zxAnVmacIfConfEntry=_ZxAnVmacIfConfEntry_Object((1,3,6,1,4,1,3902,1015,101,2,2,2,1))
zxAnVmacIfConfEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxAnVmacIfConfEntry.setStatus(_A)
_ZxAnVmacIfIndex_Type=InterfaceIndex
_ZxAnVmacIfIndex_Object=MibTableColumn
zxAnVmacIfIndex=_ZxAnVmacIfIndex_Object((1,3,6,1,4,1,3902,1015,101,2,2,2,1,1),_ZxAnVmacIfIndex_Type())
zxAnVmacIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVmacIfIndex.setStatus(_A)
class _ZxAnVmacIfConfTranslateEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ZxAnVmacIfConfTranslateEnable_Type.__name__=_C
_ZxAnVmacIfConfTranslateEnable_Object=MibTableColumn
zxAnVmacIfConfTranslateEnable=_ZxAnVmacIfConfTranslateEnable_Object((1,3,6,1,4,1,3902,1015,101,2,2,2,1,2),_ZxAnVmacIfConfTranslateEnable_Type())
zxAnVmacIfConfTranslateEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnVmacIfConfTranslateEnable.setStatus(_A)
class _ZxAnVmacIfConfTranslateLimit_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ZxAnVmacIfConfTranslateLimit_Type.__name__=_C
_ZxAnVmacIfConfTranslateLimit_Object=MibTableColumn
zxAnVmacIfConfTranslateLimit=_ZxAnVmacIfConfTranslateLimit_Object((1,3,6,1,4,1,3902,1015,101,2,2,2,1,3),_ZxAnVmacIfConfTranslateLimit_Type())
zxAnVmacIfConfTranslateLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnVmacIfConfTranslateLimit.setStatus(_A)
_ZxAnVmacIfTranslateTable_Object=MibTable
zxAnVmacIfTranslateTable=_ZxAnVmacIfTranslateTable_Object((1,3,6,1,4,1,3902,1015,101,2,2,3))
if mibBuilder.loadTexts:zxAnVmacIfTranslateTable.setStatus(_A)
_ZxAnVmacIfTranslateEntry_Object=MibTableRow
zxAnVmacIfTranslateEntry=_ZxAnVmacIfTranslateEntry_Object((1,3,6,1,4,1,3902,1015,101,2,2,3,1))
zxAnVmacIfTranslateEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:zxAnVmacIfTranslateEntry.setStatus(_A)
_ZxAnVmacIfTranslateVid_Type=VlanId
_ZxAnVmacIfTranslateVid_Object=MibTableColumn
zxAnVmacIfTranslateVid=_ZxAnVmacIfTranslateVid_Object((1,3,6,1,4,1,3902,1015,101,2,2,3,1,1),_ZxAnVmacIfTranslateVid_Type())
zxAnVmacIfTranslateVid.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVmacIfTranslateVid.setStatus(_A)
_ZxAnVmacIfTranslateSrcMac_Type=MacAddress
_ZxAnVmacIfTranslateSrcMac_Object=MibTableColumn
zxAnVmacIfTranslateSrcMac=_ZxAnVmacIfTranslateSrcMac_Object((1,3,6,1,4,1,3902,1015,101,2,2,3,1,2),_ZxAnVmacIfTranslateSrcMac_Type())
zxAnVmacIfTranslateSrcMac.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVmacIfTranslateSrcMac.setStatus(_A)
_ZxAnVmacIfTranslateVmac_Type=MacAddress
_ZxAnVmacIfTranslateVmac_Object=MibTableColumn
zxAnVmacIfTranslateVmac=_ZxAnVmacIfTranslateVmac_Object((1,3,6,1,4,1,3902,1015,101,2,2,3,1,3),_ZxAnVmacIfTranslateVmac_Type())
zxAnVmacIfTranslateVmac.setMaxAccess('read-only')
if mibBuilder.loadTexts:zxAnVmacIfTranslateVmac.setStatus(_A)
_ZxAnVmacIfTranslateRowStatus_Type=RowStatus
_ZxAnVmacIfTranslateRowStatus_Object=MibTableColumn
zxAnVmacIfTranslateRowStatus=_ZxAnVmacIfTranslateRowStatus_Object((1,3,6,1,4,1,3902,1015,101,2,2,3,1,50),_ZxAnVmacIfTranslateRowStatus_Type())
zxAnVmacIfTranslateRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVmacIfTranslateRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnVmacMib':zxAnVmacMib,'zxAnVmacObjects':zxAnVmacObjects,'zxAnVmacVlanObjects':zxAnVmacVlanObjects,'zxAnVmacVlanTable':zxAnVmacVlanTable,'zxAnVmacVlanEntry':zxAnVmacVlanEntry,_G:zxAnVmacVid,'zxAnVmacMacPoolIndex':zxAnVmacMacPoolIndex,'zxAnVmacVlanRowStatus':zxAnVmacVlanRowStatus,'zxAnVmacIfObjects':zxAnVmacIfObjects,'zxAnVmacIfConfTable':zxAnVmacIfConfTable,'zxAnVmacIfConfEntry':zxAnVmacIfConfEntry,_F:zxAnVmacIfIndex,'zxAnVmacIfConfTranslateEnable':zxAnVmacIfConfTranslateEnable,'zxAnVmacIfConfTranslateLimit':zxAnVmacIfConfTranslateLimit,'zxAnVmacIfTranslateTable':zxAnVmacIfTranslateTable,'zxAnVmacIfTranslateEntry':zxAnVmacIfTranslateEntry,_I:zxAnVmacIfTranslateVid,_J:zxAnVmacIfTranslateSrcMac,'zxAnVmacIfTranslateVmac':zxAnVmacIfTranslateVmac,'zxAnVmacIfTranslateRowStatus':zxAnVmacIfTranslateRowStatus})