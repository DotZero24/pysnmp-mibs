_N='cmauNetPrefixGroup'
_M='cmauAtmAddressGroup'
_L='axisAtmNetPrefixOperStatus'
_K='axisAtmNetPrefixAdminStatus'
_J='axisAtmAddressStatus'
_I='invalid'
_H='axisAtmAddressAtmAddress'
_G='axisAtmAddressPort'
_F='axisAtmNetPrefixPrefix'
_E='axisAtmNetPrefixPort'
_D='read-only'
_C='Integer32'
_B='CISCO-MGX82XX-ATM-UNI-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmAddress,NetPrefix=mibBuilder.importSymbols('ATM-FORUM-TC-MIB','AtmAddress','NetPrefix')
atmAddressRegistration,=mibBuilder.importSymbols('BASIS-MIB','atmAddressRegistration')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxAtmUniPortMIB=ModuleIdentity((1,3,6,1,4,1,351,150,71))
if mibBuilder.loadTexts:ciscoMgx82xxAtmUniPortMIB.setRevisions(('2003-04-18 00:00',))
_AtmNetPrefixGroup_ObjectIdentity=ObjectIdentity
atmNetPrefixGroup=_AtmNetPrefixGroup_ObjectIdentity((1,3,6,1,4,1,351,110,1,4,1,1))
_AtmNetPrefixTable_Object=MibTable
atmNetPrefixTable=_AtmNetPrefixTable_Object((1,3,6,1,4,1,351,110,1,4,1,1,1))
if mibBuilder.loadTexts:atmNetPrefixTable.setStatus(_A)
_AtmNetPrefixEntry_Object=MibTableRow
atmNetPrefixEntry=_AtmNetPrefixEntry_Object((1,3,6,1,4,1,351,110,1,4,1,1,1,1))
atmNetPrefixEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:atmNetPrefixEntry.setStatus(_A)
class _AxisAtmNetPrefixPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AxisAtmNetPrefixPort_Type.__name__=_C
_AxisAtmNetPrefixPort_Object=MibTableColumn
axisAtmNetPrefixPort=_AxisAtmNetPrefixPort_Object((1,3,6,1,4,1,351,110,1,4,1,1,1,1,1),_AxisAtmNetPrefixPort_Type())
axisAtmNetPrefixPort.setMaxAccess(_D)
if mibBuilder.loadTexts:axisAtmNetPrefixPort.setStatus(_A)
_AxisAtmNetPrefixPrefix_Type=NetPrefix
_AxisAtmNetPrefixPrefix_Object=MibTableColumn
axisAtmNetPrefixPrefix=_AxisAtmNetPrefixPrefix_Object((1,3,6,1,4,1,351,110,1,4,1,1,1,1,2),_AxisAtmNetPrefixPrefix_Type())
axisAtmNetPrefixPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:axisAtmNetPrefixPrefix.setStatus(_A)
class _AxisAtmNetPrefixAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_I,2)))
_AxisAtmNetPrefixAdminStatus_Type.__name__=_C
_AxisAtmNetPrefixAdminStatus_Object=MibTableColumn
axisAtmNetPrefixAdminStatus=_AxisAtmNetPrefixAdminStatus_Object((1,3,6,1,4,1,351,110,1,4,1,1,1,1,3),_AxisAtmNetPrefixAdminStatus_Type())
axisAtmNetPrefixAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:axisAtmNetPrefixAdminStatus.setStatus(_A)
class _AxisAtmNetPrefixOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('registering',1),('de-registering',2),('registered',3),('de-registered',4),('failRegistering',5),('failDe-registering',6)))
_AxisAtmNetPrefixOperStatus_Type.__name__=_C
_AxisAtmNetPrefixOperStatus_Object=MibTableColumn
axisAtmNetPrefixOperStatus=_AxisAtmNetPrefixOperStatus_Object((1,3,6,1,4,1,351,110,1,4,1,1,1,1,4),_AxisAtmNetPrefixOperStatus_Type())
axisAtmNetPrefixOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:axisAtmNetPrefixOperStatus.setStatus(_A)
_AtmAddressGroup_ObjectIdentity=ObjectIdentity
atmAddressGroup=_AtmAddressGroup_ObjectIdentity((1,3,6,1,4,1,351,110,1,4,1,2))
_AtmAddressTable_Object=MibTable
atmAddressTable=_AtmAddressTable_Object((1,3,6,1,4,1,351,110,1,4,1,2,1))
if mibBuilder.loadTexts:atmAddressTable.setStatus(_A)
_AtmAddressEntry_Object=MibTableRow
atmAddressEntry=_AtmAddressEntry_Object((1,3,6,1,4,1,351,110,1,4,1,2,1,1))
atmAddressEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:atmAddressEntry.setStatus(_A)
class _AxisAtmAddressPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AxisAtmAddressPort_Type.__name__=_C
_AxisAtmAddressPort_Object=MibTableColumn
axisAtmAddressPort=_AxisAtmAddressPort_Object((1,3,6,1,4,1,351,110,1,4,1,2,1,1,1),_AxisAtmAddressPort_Type())
axisAtmAddressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:axisAtmAddressPort.setStatus(_A)
_AxisAtmAddressAtmAddress_Type=AtmAddress
_AxisAtmAddressAtmAddress_Object=MibTableColumn
axisAtmAddressAtmAddress=_AxisAtmAddressAtmAddress_Object((1,3,6,1,4,1,351,110,1,4,1,2,1,1,2),_AxisAtmAddressAtmAddress_Type())
axisAtmAddressAtmAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:axisAtmAddressAtmAddress.setStatus(_A)
class _AxisAtmAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_I,2)))
_AxisAtmAddressStatus_Type.__name__=_C
_AxisAtmAddressStatus_Object=MibTableColumn
axisAtmAddressStatus=_AxisAtmAddressStatus_Object((1,3,6,1,4,1,351,110,1,4,1,2,1,1,3),_AxisAtmAddressStatus_Type())
axisAtmAddressStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:axisAtmAddressStatus.setStatus(_A)
_CmauPortMIBConformance_ObjectIdentity=ObjectIdentity
cmauPortMIBConformance=_CmauPortMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,71,2))
_CmauPortMIBGroups_ObjectIdentity=ObjectIdentity
cmauPortMIBGroups=_CmauPortMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,71,2,1))
_CmauPortMIBCompliances_ObjectIdentity=ObjectIdentity
cmauPortMIBCompliances=_CmauPortMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,71,2,2))
cmauAtmAddressGroup=ObjectGroup((1,3,6,1,4,1,351,150,71,2,1,1))
cmauAtmAddressGroup.setObjects(*((_B,_G),(_B,_H),(_B,_J)))
if mibBuilder.loadTexts:cmauAtmAddressGroup.setStatus(_A)
cmauNetPrefixGroup=ObjectGroup((1,3,6,1,4,1,351,150,71,2,1,2))
cmauNetPrefixGroup.setObjects(*((_B,_E),(_B,_F),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cmauNetPrefixGroup.setStatus(_A)
cmauPortCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,71,2,2,1))
cmauPortCompliance.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cmauPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'atmNetPrefixGroup':atmNetPrefixGroup,'atmNetPrefixTable':atmNetPrefixTable,'atmNetPrefixEntry':atmNetPrefixEntry,_E:axisAtmNetPrefixPort,_F:axisAtmNetPrefixPrefix,_K:axisAtmNetPrefixAdminStatus,_L:axisAtmNetPrefixOperStatus,'atmAddressGroup':atmAddressGroup,'atmAddressTable':atmAddressTable,'atmAddressEntry':atmAddressEntry,_G:axisAtmAddressPort,_H:axisAtmAddressAtmAddress,_J:axisAtmAddressStatus,'ciscoMgx82xxAtmUniPortMIB':ciscoMgx82xxAtmUniPortMIB,'cmauPortMIBConformance':cmauPortMIBConformance,'cmauPortMIBGroups':cmauPortMIBGroups,_M:cmauAtmAddressGroup,_N:cmauNetPrefixGroup,'cmauPortMIBCompliances':cmauPortMIBCompliances,'cmauPortCompliance':cmauPortCompliance})