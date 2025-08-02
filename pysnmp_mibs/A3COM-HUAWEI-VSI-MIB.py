_J='h3cVsiXconnectEvcSrvInstId'
_I='h3cVsiXconnectIfIndex'
_H='ethernet'
_G='h3cVsiIndex'
_F='not-accessible'
_E='OctetString'
_D='A3COM-HUAWEI-VSI-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cVsi=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,105))
if mibBuilder.loadTexts:h3cVsi.setRevisions(('2009-08-08 10:00',))
_H3cVsiObjects_ObjectIdentity=ObjectIdentity
h3cVsiObjects=_H3cVsiObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,105,1))
_H3cVsiScalarGroup_ObjectIdentity=ObjectIdentity
h3cVsiScalarGroup=_H3cVsiScalarGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,105,1,1))
_H3cVsiNextAvailableVsiIndex_Type=Unsigned32
_H3cVsiNextAvailableVsiIndex_Object=MibScalar
h3cVsiNextAvailableVsiIndex=_H3cVsiNextAvailableVsiIndex_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,1,1),_H3cVsiNextAvailableVsiIndex_Type())
h3cVsiNextAvailableVsiIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cVsiNextAvailableVsiIndex.setStatus(_A)
_H3cVsiTable_Object=MibTable
h3cVsiTable=_H3cVsiTable_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2))
if mibBuilder.loadTexts:h3cVsiTable.setStatus(_A)
_H3cVsiEntry_Object=MibTableRow
h3cVsiEntry=_H3cVsiEntry_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1))
h3cVsiEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:h3cVsiEntry.setStatus(_A)
_H3cVsiIndex_Type=Unsigned32
_H3cVsiIndex_Object=MibTableColumn
h3cVsiIndex=_H3cVsiIndex_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1,1),_H3cVsiIndex_Type())
h3cVsiIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVsiIndex.setStatus(_A)
class _H3cVsiName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cVsiName_Type.__name__=_E
_H3cVsiName_Object=MibTableColumn
h3cVsiName=_H3cVsiName_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1,2),_H3cVsiName_Type())
h3cVsiName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiName.setStatus(_A)
class _H3cVsiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('martini',1),('minm',2),('martiniAndMinm',3),('kompella',4),('kompellaAndMinm',5)))
_H3cVsiMode_Type.__name__=_C
_H3cVsiMode_Object=MibTableColumn
h3cVsiMode=_H3cVsiMode_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1,3),_H3cVsiMode_Type())
h3cVsiMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiMode.setStatus(_A)
_H3cMinmIsid_Type=Integer32
_H3cMinmIsid_Object=MibTableColumn
h3cMinmIsid=_H3cMinmIsid_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1,4),_H3cMinmIsid_Type())
h3cMinmIsid.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMinmIsid.setStatus(_A)
_H3cVsiId_Type=Unsigned32
_H3cVsiId_Object=MibTableColumn
h3cVsiId=_H3cVsiId_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1,5),_H3cVsiId_Type())
h3cVsiId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiId.setStatus(_A)
class _H3cVsiTransMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),(_H,2)))
_H3cVsiTransMode_Type.__name__=_C
_H3cVsiTransMode_Object=MibTableColumn
h3cVsiTransMode=_H3cVsiTransMode_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1,6),_H3cVsiTransMode_Type())
h3cVsiTransMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiTransMode.setStatus(_A)
class _H3cVsiEnableHubSpoke_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_H3cVsiEnableHubSpoke_Type.__name__=_C
_H3cVsiEnableHubSpoke_Object=MibTableColumn
h3cVsiEnableHubSpoke=_H3cVsiEnableHubSpoke_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1,7),_H3cVsiEnableHubSpoke_Type())
h3cVsiEnableHubSpoke.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiEnableHubSpoke.setStatus(_A)
class _H3cVsiAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminUp',1),('adminDown',2)))
_H3cVsiAdminState_Type.__name__=_C
_H3cVsiAdminState_Object=MibTableColumn
h3cVsiAdminState=_H3cVsiAdminState_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1,8),_H3cVsiAdminState_Type())
h3cVsiAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiAdminState.setStatus(_A)
_H3cVsiRowStatus_Type=RowStatus
_H3cVsiRowStatus_Object=MibTableColumn
h3cVsiRowStatus=_H3cVsiRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,2,1,9),_H3cVsiRowStatus_Type())
h3cVsiRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiRowStatus.setStatus(_A)
_H3cVsiXconnectTable_Object=MibTable
h3cVsiXconnectTable=_H3cVsiXconnectTable_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,3))
if mibBuilder.loadTexts:h3cVsiXconnectTable.setStatus(_A)
_H3cVsiXconnectEntry_Object=MibTableRow
h3cVsiXconnectEntry=_H3cVsiXconnectEntry_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,3,1))
h3cVsiXconnectEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:h3cVsiXconnectEntry.setStatus(_A)
_H3cVsiXconnectIfIndex_Type=Unsigned32
_H3cVsiXconnectIfIndex_Object=MibTableColumn
h3cVsiXconnectIfIndex=_H3cVsiXconnectIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,3,1,1),_H3cVsiXconnectIfIndex_Type())
h3cVsiXconnectIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVsiXconnectIfIndex.setStatus(_A)
_H3cVsiXconnectEvcSrvInstId_Type=Unsigned32
_H3cVsiXconnectEvcSrvInstId_Object=MibTableColumn
h3cVsiXconnectEvcSrvInstId=_H3cVsiXconnectEvcSrvInstId_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,3,1,2),_H3cVsiXconnectEvcSrvInstId_Type())
h3cVsiXconnectEvcSrvInstId.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVsiXconnectEvcSrvInstId.setStatus(_A)
class _H3cVsiXconnectVsiName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cVsiXconnectVsiName_Type.__name__=_E
_H3cVsiXconnectVsiName_Object=MibTableColumn
h3cVsiXconnectVsiName=_H3cVsiXconnectVsiName_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,3,1,3),_H3cVsiXconnectVsiName_Type())
h3cVsiXconnectVsiName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiXconnectVsiName.setStatus(_A)
class _H3cVsiXconnectAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),(_H,2)))
_H3cVsiXconnectAccessMode_Type.__name__=_C
_H3cVsiXconnectAccessMode_Object=MibTableColumn
h3cVsiXconnectAccessMode=_H3cVsiXconnectAccessMode_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,3,1,4),_H3cVsiXconnectAccessMode_Type())
h3cVsiXconnectAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiXconnectAccessMode.setStatus(_A)
class _H3cVsiXconnectHubSpoke_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('hub',2),('spoke',3)))
_H3cVsiXconnectHubSpoke_Type.__name__=_C
_H3cVsiXconnectHubSpoke_Object=MibTableColumn
h3cVsiXconnectHubSpoke=_H3cVsiXconnectHubSpoke_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,3,1,5),_H3cVsiXconnectHubSpoke_Type())
h3cVsiXconnectHubSpoke.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiXconnectHubSpoke.setStatus(_A)
_H3cVsiXconnectRowStatus_Type=RowStatus
_H3cVsiXconnectRowStatus_Object=MibTableColumn
h3cVsiXconnectRowStatus=_H3cVsiXconnectRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,105,1,3,1,6),_H3cVsiXconnectRowStatus_Type())
h3cVsiXconnectRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVsiXconnectRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cVsi':h3cVsi,'h3cVsiObjects':h3cVsiObjects,'h3cVsiScalarGroup':h3cVsiScalarGroup,'h3cVsiNextAvailableVsiIndex':h3cVsiNextAvailableVsiIndex,'h3cVsiTable':h3cVsiTable,'h3cVsiEntry':h3cVsiEntry,_G:h3cVsiIndex,'h3cVsiName':h3cVsiName,'h3cVsiMode':h3cVsiMode,'h3cMinmIsid':h3cMinmIsid,'h3cVsiId':h3cVsiId,'h3cVsiTransMode':h3cVsiTransMode,'h3cVsiEnableHubSpoke':h3cVsiEnableHubSpoke,'h3cVsiAdminState':h3cVsiAdminState,'h3cVsiRowStatus':h3cVsiRowStatus,'h3cVsiXconnectTable':h3cVsiXconnectTable,'h3cVsiXconnectEntry':h3cVsiXconnectEntry,_I:h3cVsiXconnectIfIndex,_J:h3cVsiXconnectEvcSrvInstId,'h3cVsiXconnectVsiName':h3cVsiXconnectVsiName,'h3cVsiXconnectAccessMode':h3cVsiXconnectAccessMode,'h3cVsiXconnectHubSpoke':h3cVsiXconnectHubSpoke,'h3cVsiXconnectRowStatus':h3cVsiXconnectRowStatus})