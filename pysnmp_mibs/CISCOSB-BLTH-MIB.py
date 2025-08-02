_E='rlBlthIfIndex'
_D='CISCOSB-BLTH-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlBlth=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,246))
if mibBuilder.loadTexts:rlBlth.setRevisions(('2022-04-30 00:00',))
_RlBlthIfTable_Object=MibTable
rlBlthIfTable=_RlBlthIfTable_Object((1,3,6,1,4,1,9,6,1,101,246,1))
if mibBuilder.loadTexts:rlBlthIfTable.setStatus(_A)
_RlBlthIfTableEntry_Object=MibTableRow
rlBlthIfTableEntry=_RlBlthIfTableEntry_Object((1,3,6,1,4,1,9,6,1,101,246,1,1))
rlBlthIfTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlBlthIfTableEntry.setStatus(_A)
_RlBlthIfIndex_Type=InterfaceIndex
_RlBlthIfIndex_Object=MibTableColumn
rlBlthIfIndex=_RlBlthIfIndex_Object((1,3,6,1,4,1,9,6,1,101,246,1,1,1),_RlBlthIfIndex_Type())
rlBlthIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlBlthIfIndex.setStatus(_A)
_RlBlthPin_Type=DisplayString
_RlBlthPin_Object=MibTableColumn
rlBlthPin=_RlBlthPin_Object((1,3,6,1,4,1,9,6,1,101,246,1,1,2),_RlBlthPin_Type())
rlBlthPin.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBlthPin.setStatus(_A)
_RlBlthDeviceName_Type=DisplayString
_RlBlthDeviceName_Object=MibTableColumn
rlBlthDeviceName=_RlBlthDeviceName_Object((1,3,6,1,4,1,9,6,1,101,246,1,1,3),_RlBlthDeviceName_Type())
rlBlthDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBlthDeviceName.setStatus(_A)
_RlBlthDongleMAC_Type=MacAddress
_RlBlthDongleMAC_Object=MibTableColumn
rlBlthDongleMAC=_RlBlthDongleMAC_Object((1,3,6,1,4,1,9,6,1,101,246,1,1,4),_RlBlthDongleMAC_Type())
rlBlthDongleMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBlthDongleMAC.setStatus(_A)
class _RlBlthDonglePresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_RlBlthDonglePresent_Type.__name__=_C
_RlBlthDonglePresent_Object=MibTableColumn
rlBlthDonglePresent=_RlBlthDonglePresent_Object((1,3,6,1,4,1,9,6,1,101,246,1,1,5),_RlBlthDonglePresent_Type())
rlBlthDonglePresent.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBlthDonglePresent.setStatus(_A)
_RlBlthBus_Type=DisplayString
_RlBlthBus_Object=MibTableColumn
rlBlthBus=_RlBlthBus_Object((1,3,6,1,4,1,9,6,1,101,246,1,1,6),_RlBlthBus_Type())
rlBlthBus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBlthBus.setStatus(_A)
class _RlBlthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notready',0),('discoverable',1),('connected',2),('admindown',3)))
_RlBlthState_Type.__name__=_C
_RlBlthState_Object=MibTableColumn
rlBlthState=_RlBlthState_Object((1,3,6,1,4,1,9,6,1,101,246,1,1,7),_RlBlthState_Type())
rlBlthState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBlthState.setStatus(_A)
_RlBlthPartnerName_Type=DisplayString
_RlBlthPartnerName_Object=MibTableColumn
rlBlthPartnerName=_RlBlthPartnerName_Object((1,3,6,1,4,1,9,6,1,101,246,1,1,8),_RlBlthPartnerName_Type())
rlBlthPartnerName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBlthPartnerName.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rlBlth':rlBlth,'rlBlthIfTable':rlBlthIfTable,'rlBlthIfTableEntry':rlBlthIfTableEntry,_E:rlBlthIfIndex,'rlBlthPin':rlBlthPin,'rlBlthDeviceName':rlBlthDeviceName,'rlBlthDongleMAC':rlBlthDongleMAC,'rlBlthDonglePresent':rlBlthDonglePresent,'rlBlthBus':rlBlthBus,'rlBlthState':rlBlthState,'rlBlthPartnerName':rlBlthPartnerName})