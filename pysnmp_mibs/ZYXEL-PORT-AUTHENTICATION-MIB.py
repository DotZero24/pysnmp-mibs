_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelPortAuthentication=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,62))
_ZyxelPortAuthenticationSetup_ObjectIdentity=ObjectIdentity
zyxelPortAuthenticationSetup=_ZyxelPortAuthenticationSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,62,1))
_ZyPortAuthenticationState_Type=EnabledStatus
_ZyPortAuthenticationState_Object=MibScalar
zyPortAuthenticationState=_ZyPortAuthenticationState_Object((1,3,6,1,4,1,890,1,15,3,62,1,1),_ZyPortAuthenticationState_Type())
zyPortAuthenticationState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationState.setStatus(_A)
_ZyxelPortAuthenticationPortTable_Object=MibTable
zyxelPortAuthenticationPortTable=_ZyxelPortAuthenticationPortTable_Object((1,3,6,1,4,1,890,1,15,3,62,1,2))
if mibBuilder.loadTexts:zyxelPortAuthenticationPortTable.setStatus(_A)
_ZyxelPortAuthenticationPortEntry_Object=MibTableRow
zyxelPortAuthenticationPortEntry=_ZyxelPortAuthenticationPortEntry_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1))
zyxelPortAuthenticationPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelPortAuthenticationPortEntry.setStatus(_A)
_ZyPortAuthenticationPortState_Type=EnabledStatus
_ZyPortAuthenticationPortState_Object=MibTableColumn
zyPortAuthenticationPortState=_ZyPortAuthenticationPortState_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,1),_ZyPortAuthenticationPortState_Type())
zyPortAuthenticationPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortState.setStatus(_A)
_ZyPortReAuthenticationPortState_Type=EnabledStatus
_ZyPortReAuthenticationPortState_Object=MibTableColumn
zyPortReAuthenticationPortState=_ZyPortReAuthenticationPortState_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,2),_ZyPortReAuthenticationPortState_Type())
zyPortReAuthenticationPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortReAuthenticationPortState.setStatus(_A)
_ZyPortReAuthenticationPortTimer_Type=Integer32
_ZyPortReAuthenticationPortTimer_Object=MibTableColumn
zyPortReAuthenticationPortTimer=_ZyPortReAuthenticationPortTimer_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,3),_ZyPortReAuthenticationPortTimer_Type())
zyPortReAuthenticationPortTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortReAuthenticationPortTimer.setStatus(_A)
_ZyPortAuthenticationPortQuietPeriod_Type=Integer32
_ZyPortAuthenticationPortQuietPeriod_Object=MibTableColumn
zyPortAuthenticationPortQuietPeriod=_ZyPortAuthenticationPortQuietPeriod_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,4),_ZyPortAuthenticationPortQuietPeriod_Type())
zyPortAuthenticationPortQuietPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortQuietPeriod.setStatus(_A)
_ZyPortAuthenticationPortTxPeriod_Type=Integer32
_ZyPortAuthenticationPortTxPeriod_Object=MibTableColumn
zyPortAuthenticationPortTxPeriod=_ZyPortAuthenticationPortTxPeriod_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,5),_ZyPortAuthenticationPortTxPeriod_Type())
zyPortAuthenticationPortTxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortTxPeriod.setStatus(_A)
_ZyPortAuthenticationPortSupplicantTimeout_Type=Integer32
_ZyPortAuthenticationPortSupplicantTimeout_Object=MibTableColumn
zyPortAuthenticationPortSupplicantTimeout=_ZyPortAuthenticationPortSupplicantTimeout_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,6),_ZyPortAuthenticationPortSupplicantTimeout_Type())
zyPortAuthenticationPortSupplicantTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortSupplicantTimeout.setStatus(_A)
_ZyPortAuthenticationPortMaxRequest_Type=Integer32
_ZyPortAuthenticationPortMaxRequest_Object=MibTableColumn
zyPortAuthenticationPortMaxRequest=_ZyPortAuthenticationPortMaxRequest_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,7),_ZyPortAuthenticationPortMaxRequest_Type())
zyPortAuthenticationPortMaxRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortMaxRequest.setStatus(_A)
_ZyPortAuthenticationPortGuestVlanState_Type=EnabledStatus
_ZyPortAuthenticationPortGuestVlanState_Object=MibTableColumn
zyPortAuthenticationPortGuestVlanState=_ZyPortAuthenticationPortGuestVlanState_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,8),_ZyPortAuthenticationPortGuestVlanState_Type())
zyPortAuthenticationPortGuestVlanState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortGuestVlanState.setStatus(_A)
_ZyPortAuthenticationPortGuestVlan_Type=Integer32
_ZyPortAuthenticationPortGuestVlan_Object=MibTableColumn
zyPortAuthenticationPortGuestVlan=_ZyPortAuthenticationPortGuestVlan_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,9),_ZyPortAuthenticationPortGuestVlan_Type())
zyPortAuthenticationPortGuestVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortGuestVlan.setStatus(_A)
class _ZyPortAuthenticationPortGuestVlanHostMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('multiHost',0),('multiSecure',1)))
_ZyPortAuthenticationPortGuestVlanHostMode_Type.__name__=_C
_ZyPortAuthenticationPortGuestVlanHostMode_Object=MibTableColumn
zyPortAuthenticationPortGuestVlanHostMode=_ZyPortAuthenticationPortGuestVlanHostMode_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,10),_ZyPortAuthenticationPortGuestVlanHostMode_Type())
zyPortAuthenticationPortGuestVlanHostMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortGuestVlanHostMode.setStatus(_A)
_ZyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber_Type=Integer32
_ZyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber_Object=MibTableColumn
zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber=_ZyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,11),_ZyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber_Type())
zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber.setStatus(_A)
class _ZyPortAuthenticationPortCompoundAuthenticationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('strict',0),('loose',1)))
_ZyPortAuthenticationPortCompoundAuthenticationMode_Type.__name__=_C
_ZyPortAuthenticationPortCompoundAuthenticationMode_Object=MibTableColumn
zyPortAuthenticationPortCompoundAuthenticationMode=_ZyPortAuthenticationPortCompoundAuthenticationMode_Object((1,3,6,1,4,1,890,1,15,3,62,1,2,1,12),_ZyPortAuthenticationPortCompoundAuthenticationMode_Type())
zyPortAuthenticationPortCompoundAuthenticationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationPortCompoundAuthenticationMode.setStatus(_A)
_ZyPortAuthenticationEapolFloodState_Type=EnabledStatus
_ZyPortAuthenticationEapolFloodState_Object=MibScalar
zyPortAuthenticationEapolFloodState=_ZyPortAuthenticationEapolFloodState_Object((1,3,6,1,4,1,890,1,15,3,62,1,3),_ZyPortAuthenticationEapolFloodState_Type())
zyPortAuthenticationEapolFloodState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortAuthenticationEapolFloodState.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-PORT-AUTHENTICATION-MIB',**{'zyxelPortAuthentication':zyxelPortAuthentication,'zyxelPortAuthenticationSetup':zyxelPortAuthenticationSetup,'zyPortAuthenticationState':zyPortAuthenticationState,'zyxelPortAuthenticationPortTable':zyxelPortAuthenticationPortTable,'zyxelPortAuthenticationPortEntry':zyxelPortAuthenticationPortEntry,'zyPortAuthenticationPortState':zyPortAuthenticationPortState,'zyPortReAuthenticationPortState':zyPortReAuthenticationPortState,'zyPortReAuthenticationPortTimer':zyPortReAuthenticationPortTimer,'zyPortAuthenticationPortQuietPeriod':zyPortAuthenticationPortQuietPeriod,'zyPortAuthenticationPortTxPeriod':zyPortAuthenticationPortTxPeriod,'zyPortAuthenticationPortSupplicantTimeout':zyPortAuthenticationPortSupplicantTimeout,'zyPortAuthenticationPortMaxRequest':zyPortAuthenticationPortMaxRequest,'zyPortAuthenticationPortGuestVlanState':zyPortAuthenticationPortGuestVlanState,'zyPortAuthenticationPortGuestVlan':zyPortAuthenticationPortGuestVlan,'zyPortAuthenticationPortGuestVlanHostMode':zyPortAuthenticationPortGuestVlanHostMode,'zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber':zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber,'zyPortAuthenticationPortCompoundAuthenticationMode':zyPortAuthenticationPortCompoundAuthenticationMode,'zyPortAuthenticationEapolFloodState':zyPortAuthenticationEapolFloodState})