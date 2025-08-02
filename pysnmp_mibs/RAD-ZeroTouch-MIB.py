_J='bootstrapDeviceHwVer'
_I='bootstrapDeviceSwVer'
_H='bootstrapDeviceMac'
_G='bootstrapDeviceType'
_F='read-write'
_E='bootstrapIfIndex'
_D='Integer32'
_C='read-only'
_B='RAD-ZeroTouch-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
systemsEvents,=mibBuilder.importSymbols('RAD-GEN-MIB','systemsEvents')
systems,=mibBuilder.importSymbols('RAD-SMI-MIB','systems')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
radZeroTouch=ModuleIdentity((1,3,6,1,4,1,164,6,1,17))
_BootstrapTable_Object=MibTable
bootstrapTable=_BootstrapTable_Object((1,3,6,1,4,1,164,6,1,17,1))
if mibBuilder.loadTexts:bootstrapTable.setStatus(_A)
_BootstrapEntry_Object=MibTableRow
bootstrapEntry=_BootstrapEntry_Object((1,3,6,1,4,1,164,6,1,17,1,1))
bootstrapEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:bootstrapEntry.setStatus(_A)
_BootstrapIfIndex_Type=Integer32
_BootstrapIfIndex_Object=MibTableColumn
bootstrapIfIndex=_BootstrapIfIndex_Object((1,3,6,1,4,1,164,6,1,17,1,1,1),_BootstrapIfIndex_Type())
bootstrapIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bootstrapIfIndex.setStatus(_A)
_BootstrapDeviceType_Type=ObjectIdentifier
_BootstrapDeviceType_Object=MibTableColumn
bootstrapDeviceType=_BootstrapDeviceType_Object((1,3,6,1,4,1,164,6,1,17,1,1,2),_BootstrapDeviceType_Type())
bootstrapDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:bootstrapDeviceType.setStatus(_A)
_BootstrapDeviceMac_Type=MacAddress
_BootstrapDeviceMac_Object=MibTableColumn
bootstrapDeviceMac=_BootstrapDeviceMac_Object((1,3,6,1,4,1,164,6,1,17,1,1,3),_BootstrapDeviceMac_Type())
bootstrapDeviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:bootstrapDeviceMac.setStatus(_A)
_BootstrapDeviceSwVer_Type=SnmpAdminString
_BootstrapDeviceSwVer_Object=MibTableColumn
bootstrapDeviceSwVer=_BootstrapDeviceSwVer_Object((1,3,6,1,4,1,164,6,1,17,1,1,4),_BootstrapDeviceSwVer_Type())
bootstrapDeviceSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:bootstrapDeviceSwVer.setStatus(_A)
_BootstrapDeviceHwVer_Type=SnmpAdminString
_BootstrapDeviceHwVer_Object=MibTableColumn
bootstrapDeviceHwVer=_BootstrapDeviceHwVer_Object((1,3,6,1,4,1,164,6,1,17,1,1,5),_BootstrapDeviceHwVer_Type())
bootstrapDeviceHwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:bootstrapDeviceHwVer.setStatus(_A)
class _BootstrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('on',2),('acknowledge',3)))
_BootstrapState_Type.__name__=_D
_BootstrapState_Object=MibTableColumn
bootstrapState=_BootstrapState_Object((1,3,6,1,4,1,164,6,1,17,1,1,6),_BootstrapState_Type())
bootstrapState.setMaxAccess(_F)
if mibBuilder.loadTexts:bootstrapState.setStatus(_A)
class _BootstrapActivationCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('off',2),('on',3)))
_BootstrapActivationCmd_Type.__name__=_D
_BootstrapActivationCmd_Object=MibScalar
bootstrapActivationCmd=_BootstrapActivationCmd_Object((1,3,6,1,4,1,164,6,1,17,2),_BootstrapActivationCmd_Type())
bootstrapActivationCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:bootstrapActivationCmd.setStatus(_A)
systemBootstrap=NotificationType((1,3,6,1,4,1,164,6,1,0,85))
systemBootstrap.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:systemBootstrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'systemBootstrap':systemBootstrap,'radZeroTouch':radZeroTouch,'bootstrapTable':bootstrapTable,'bootstrapEntry':bootstrapEntry,_E:bootstrapIfIndex,_G:bootstrapDeviceType,_H:bootstrapDeviceMac,_I:bootstrapDeviceSwVer,_J:bootstrapDeviceHwVer,'bootstrapState':bootstrapState,'bootstrapActivationCmd':bootstrapActivationCmd})