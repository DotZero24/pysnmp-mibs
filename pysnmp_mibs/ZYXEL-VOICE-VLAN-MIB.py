_G='not-accessible'
_F='zyVoiceVlanOUIMask'
_E='zyVoiceVlanOUIAddress'
_D='ZYXEL-VOICE-VLAN-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelVoiceVlan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,96))
_ZyxelVoiceVlanSetup_ObjectIdentity=ObjectIdentity
zyxelVoiceVlanSetup=_ZyxelVoiceVlanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,96,1))
class _ZyxelVoiceVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZyxelVoiceVlanID_Type.__name__=_C
_ZyxelVoiceVlanID_Object=MibScalar
zyxelVoiceVlanID=_ZyxelVoiceVlanID_Object((1,3,6,1,4,1,890,1,15,3,96,1,1),_ZyxelVoiceVlanID_Type())
zyxelVoiceVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:zyxelVoiceVlanID.setStatus(_A)
class _ZyxelVoiceVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZyxelVoiceVlanPriority_Type.__name__=_C
_ZyxelVoiceVlanPriority_Object=MibScalar
zyxelVoiceVlanPriority=_ZyxelVoiceVlanPriority_Object((1,3,6,1,4,1,890,1,15,3,96,1,2),_ZyxelVoiceVlanPriority_Type())
zyxelVoiceVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zyxelVoiceVlanPriority.setStatus(_A)
_ZyxelVoiceVlanMaxNumberOfOUI_Type=Integer32
_ZyxelVoiceVlanMaxNumberOfOUI_Object=MibScalar
zyxelVoiceVlanMaxNumberOfOUI=_ZyxelVoiceVlanMaxNumberOfOUI_Object((1,3,6,1,4,1,890,1,15,3,96,1,5),_ZyxelVoiceVlanMaxNumberOfOUI_Type())
zyxelVoiceVlanMaxNumberOfOUI.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyxelVoiceVlanMaxNumberOfOUI.setStatus(_A)
_ZyxelVoiceVlanOUITable_Object=MibTable
zyxelVoiceVlanOUITable=_ZyxelVoiceVlanOUITable_Object((1,3,6,1,4,1,890,1,15,3,96,1,6))
if mibBuilder.loadTexts:zyxelVoiceVlanOUITable.setStatus(_A)
_ZyxelVoiceVlanOUIEntry_Object=MibTableRow
zyxelVoiceVlanOUIEntry=_ZyxelVoiceVlanOUIEntry_Object((1,3,6,1,4,1,890,1,15,3,96,1,6,1))
zyxelVoiceVlanOUIEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:zyxelVoiceVlanOUIEntry.setStatus(_A)
_ZyVoiceVlanOUIAddress_Type=MacAddress
_ZyVoiceVlanOUIAddress_Object=MibTableColumn
zyVoiceVlanOUIAddress=_ZyVoiceVlanOUIAddress_Object((1,3,6,1,4,1,890,1,15,3,96,1,6,1,1),_ZyVoiceVlanOUIAddress_Type())
zyVoiceVlanOUIAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:zyVoiceVlanOUIAddress.setStatus(_A)
_ZyVoiceVlanOUIMask_Type=MacAddress
_ZyVoiceVlanOUIMask_Object=MibTableColumn
zyVoiceVlanOUIMask=_ZyVoiceVlanOUIMask_Object((1,3,6,1,4,1,890,1,15,3,96,1,6,1,2),_ZyVoiceVlanOUIMask_Type())
zyVoiceVlanOUIMask.setMaxAccess(_G)
if mibBuilder.loadTexts:zyVoiceVlanOUIMask.setStatus(_A)
_ZyVoiceVlanOUIDescription_Type=DisplayString
_ZyVoiceVlanOUIDescription_Object=MibTableColumn
zyVoiceVlanOUIDescription=_ZyVoiceVlanOUIDescription_Object((1,3,6,1,4,1,890,1,15,3,96,1,6,1,3),_ZyVoiceVlanOUIDescription_Type())
zyVoiceVlanOUIDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVoiceVlanOUIDescription.setStatus(_A)
_ZyVoiceVlanOUIRowStatus_Type=RowStatus
_ZyVoiceVlanOUIRowStatus_Object=MibTableColumn
zyVoiceVlanOUIRowStatus=_ZyVoiceVlanOUIRowStatus_Object((1,3,6,1,4,1,890,1,15,3,96,1,6,1,4),_ZyVoiceVlanOUIRowStatus_Type())
zyVoiceVlanOUIRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVoiceVlanOUIRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelVoiceVlan':zyxelVoiceVlan,'zyxelVoiceVlanSetup':zyxelVoiceVlanSetup,'zyxelVoiceVlanID':zyxelVoiceVlanID,'zyxelVoiceVlanPriority':zyxelVoiceVlanPriority,'zyxelVoiceVlanMaxNumberOfOUI':zyxelVoiceVlanMaxNumberOfOUI,'zyxelVoiceVlanOUITable':zyxelVoiceVlanOUITable,'zyxelVoiceVlanOUIEntry':zyxelVoiceVlanOUIEntry,_E:zyVoiceVlanOUIAddress,_F:zyVoiceVlanOUIMask,'zyVoiceVlanOUIDescription':zyVoiceVlanOUIDescription,'zyVoiceVlanOUIRowStatus':zyVoiceVlanOUIRowStatus})