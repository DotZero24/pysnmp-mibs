_J='adGenArpInnerVlan'
_I='adGenArpOuterVlan'
_H='adGenArpIpAddress'
_G='Integer32'
_F='OctetString'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='ADTRAN-ARP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adGenArp,adGenArpID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenArp','adGenArpID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adTa5kArpModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,30,1))
_AdGenArpTable_Object=MibTable
adGenArpTable=_AdGenArpTable_Object((1,3,6,1,4,1,664,5,67,1,30,1))
if mibBuilder.loadTexts:adGenArpTable.setStatus(_A)
_AdGenArpEntry_Object=MibTableRow
adGenArpEntry=_AdGenArpEntry_Object((1,3,6,1,4,1,664,5,67,1,30,1,1))
adGenArpEntry.setIndexNames((0,_D,_E),(0,_C,_H),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:adGenArpEntry.setStatus(_A)
_AdGenArpIpAddress_Type=IpAddress
_AdGenArpIpAddress_Object=MibTableColumn
adGenArpIpAddress=_AdGenArpIpAddress_Object((1,3,6,1,4,1,664,5,67,1,30,1,1,1),_AdGenArpIpAddress_Type())
adGenArpIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenArpIpAddress.setStatus(_A)
_AdGenArpOuterVlan_Type=Integer32
_AdGenArpOuterVlan_Object=MibTableColumn
adGenArpOuterVlan=_AdGenArpOuterVlan_Object((1,3,6,1,4,1,664,5,67,1,30,1,1,2),_AdGenArpOuterVlan_Type())
adGenArpOuterVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenArpOuterVlan.setStatus(_A)
_AdGenArpInnerVlan_Type=Integer32
_AdGenArpInnerVlan_Object=MibTableColumn
adGenArpInnerVlan=_AdGenArpInnerVlan_Object((1,3,6,1,4,1,664,5,67,1,30,1,1,3),_AdGenArpInnerVlan_Type())
adGenArpInnerVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenArpInnerVlan.setStatus(_A)
class _AdGenArpMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AdGenArpMacAddress_Type.__name__=_F
_AdGenArpMacAddress_Object=MibTableColumn
adGenArpMacAddress=_AdGenArpMacAddress_Object((1,3,6,1,4,1,664,5,67,1,30,1,1,4),_AdGenArpMacAddress_Type())
adGenArpMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenArpMacAddress.setStatus(_A)
_AdGenArpTTLMin_Type=Integer32
_AdGenArpTTLMin_Object=MibTableColumn
adGenArpTTLMin=_AdGenArpTTLMin_Object((1,3,6,1,4,1,664,5,67,1,30,1,1,5),_AdGenArpTTLMin_Type())
adGenArpTTLMin.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenArpTTLMin.setStatus(_A)
_AdGenArpInterface_Type=DisplayString
_AdGenArpInterface_Object=MibTableColumn
adGenArpInterface=_AdGenArpInterface_Object((1,3,6,1,4,1,664,5,67,1,30,1,1,6),_AdGenArpInterface_Type())
adGenArpInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenArpInterface.setStatus(_A)
class _AdGenArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('invalid',2),('dynamic',3),('static',4),('proxy',5),('reachable',6),('stale',7),('incomplete',8)))
_AdGenArpType_Type.__name__=_G
_AdGenArpType_Object=MibTableColumn
adGenArpType=_AdGenArpType_Object((1,3,6,1,4,1,664,5,67,1,30,1,1,7),_AdGenArpType_Type())
adGenArpType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenArpType.setStatus(_A)
_AdGenArpSettingsTable_Object=MibTable
adGenArpSettingsTable=_AdGenArpSettingsTable_Object((1,3,6,1,4,1,664,5,67,1,30,2))
if mibBuilder.loadTexts:adGenArpSettingsTable.setStatus(_A)
_AdGenArpSettingsEntry_Object=MibTableRow
adGenArpSettingsEntry=_AdGenArpSettingsEntry_Object((1,3,6,1,4,1,664,5,67,1,30,2,1))
adGenArpSettingsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenArpSettingsEntry.setStatus(_A)
_AdGenArpTimeout_Type=Integer32
_AdGenArpTimeout_Object=MibTableColumn
adGenArpTimeout=_AdGenArpTimeout_Object((1,3,6,1,4,1,664,5,67,1,30,2,1,1),_AdGenArpTimeout_Type())
adGenArpTimeout.setMaxAccess('read-write')
if mibBuilder.loadTexts:adGenArpTimeout.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'adGenArpTable':adGenArpTable,'adGenArpEntry':adGenArpEntry,_H:adGenArpIpAddress,_I:adGenArpOuterVlan,_J:adGenArpInnerVlan,'adGenArpMacAddress':adGenArpMacAddress,'adGenArpTTLMin':adGenArpTTLMin,'adGenArpInterface':adGenArpInterface,'adGenArpType':adGenArpType,'adGenArpSettingsTable':adGenArpSettingsTable,'adGenArpSettingsEntry':adGenArpSettingsEntry,'adGenArpTimeout':adGenArpTimeout,'adTa5kArpModuleIdentity':adTa5kArpModuleIdentity})