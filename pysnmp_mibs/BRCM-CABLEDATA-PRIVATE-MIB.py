_F='read-create'
_E='cdPvtMibEnableKeyIndex'
_D='BRCM-CABLEDATA-PRIVATE-MIB'
_C='OctetString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataPrivate,=mibBuilder.importSymbols('BRCM-CABLEDATA-SMI','cableDataPrivate')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
cableDataPrivateMIB=ModuleIdentity((1,3,6,1,4,1,4413,2,99,1))
if mibBuilder.loadTexts:cableDataPrivateMIB.setRevisions(('2007-02-05 00:00','2002-06-04 00:00'))
_CableDataPrivateMIBObjects_ObjectIdentity=ObjectIdentity
cableDataPrivateMIBObjects=_CableDataPrivateMIBObjects_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1))
_CableDataPrivateBase_ObjectIdentity=ObjectIdentity
cableDataPrivateBase=_CableDataPrivateBase_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,1))
class _CdPrivateMibEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('factory',1),('engineering',2)))
_CdPrivateMibEnable_Type.__name__=_B
_CdPrivateMibEnable_Object=MibScalar
cdPrivateMibEnable=_CdPrivateMibEnable_Object((1,3,6,1,4,1,4413,2,99,1,1,1,1),_CdPrivateMibEnable_Type())
cdPrivateMibEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cdPrivateMibEnable.setStatus(_A)
_CdPrivateMibEnableKeyTable_Object=MibTable
cdPrivateMibEnableKeyTable=_CdPrivateMibEnableKeyTable_Object((1,3,6,1,4,1,4413,2,99,1,1,1,2))
if mibBuilder.loadTexts:cdPrivateMibEnableKeyTable.setStatus(_A)
_CdPrivateMibEnableKeyEntry_Object=MibTableRow
cdPrivateMibEnableKeyEntry=_CdPrivateMibEnableKeyEntry_Object((1,3,6,1,4,1,4413,2,99,1,1,1,2,1))
cdPrivateMibEnableKeyEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cdPrivateMibEnableKeyEntry.setStatus(_A)
class _CdPvtMibEnableKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CdPvtMibEnableKeyIndex_Type.__name__=_B
_CdPvtMibEnableKeyIndex_Object=MibTableColumn
cdPvtMibEnableKeyIndex=_CdPvtMibEnableKeyIndex_Object((1,3,6,1,4,1,4413,2,99,1,1,1,2,1,1),_CdPvtMibEnableKeyIndex_Type())
cdPvtMibEnableKeyIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cdPvtMibEnableKeyIndex.setStatus(_A)
class _CdPvtMibEnableKeyValue_Type(OctetString):defaultValue=OctetString('')
_CdPvtMibEnableKeyValue_Type.__name__=_C
_CdPvtMibEnableKeyValue_Object=MibTableColumn
cdPvtMibEnableKeyValue=_CdPvtMibEnableKeyValue_Object((1,3,6,1,4,1,4413,2,99,1,1,1,2,1,2),_CdPvtMibEnableKeyValue_Type())
cdPvtMibEnableKeyValue.setMaxAccess(_F)
if mibBuilder.loadTexts:cdPvtMibEnableKeyValue.setStatus(_A)
_CdPvtMibEnableKeyStatus_Type=RowStatus
_CdPvtMibEnableKeyStatus_Object=MibTableColumn
cdPvtMibEnableKeyStatus=_CdPvtMibEnableKeyStatus_Object((1,3,6,1,4,1,4413,2,99,1,1,1,2,1,3),_CdPvtMibEnableKeyStatus_Type())
cdPvtMibEnableKeyStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cdPvtMibEnableKeyStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cableDataPrivateMIB':cableDataPrivateMIB,'cableDataPrivateMIBObjects':cableDataPrivateMIBObjects,'cableDataPrivateBase':cableDataPrivateBase,'cdPrivateMibEnable':cdPrivateMibEnable,'cdPrivateMibEnableKeyTable':cdPrivateMibEnableKeyTable,'cdPrivateMibEnableKeyEntry':cdPrivateMibEnableKeyEntry,_E:cdPvtMibEnableKeyIndex,'cdPvtMibEnableKeyValue':cdPvtMibEnableKeyValue,'cdPvtMibEnableKeyStatus':cdPvtMibEnableKeyStatus})