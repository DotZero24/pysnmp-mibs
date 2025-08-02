_E='communityIndex'
_D='COMMUNITY-MIB'
_C='OctetString'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_CommsDevice_ObjectIdentity=ObjectIdentity
commsDevice=_CommsDevice_ObjectIdentity((1,3,6,1,4,1,52,1))
_Community_ObjectIdentity=ObjectIdentity
community=_Community_ObjectIdentity((1,3,6,1,4,1,52,1,52))
_CommunityTable_Object=MibTable
communityTable=_CommunityTable_Object((1,3,6,1,4,1,52,1,52,2))
if mibBuilder.loadTexts:communityTable.setStatus(_A)
_CommunityEntry_Object=MibTableRow
communityEntry=_CommunityEntry_Object((1,3,6,1,4,1,52,1,52,2,1))
communityEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:communityEntry.setStatus(_A)
class _CommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CommunityName_Type.__name__=_C
_CommunityName_Object=MibTableColumn
communityName=_CommunityName_Object((1,3,6,1,4,1,52,1,52,2,1,1),_CommunityName_Type())
communityName.setMaxAccess(_B)
if mibBuilder.loadTexts:communityName.setStatus(_A)
_CommunityTrap_Type=Integer32
_CommunityTrap_Object=MibTableColumn
communityTrap=_CommunityTrap_Object((1,3,6,1,4,1,52,1,52,2,1,2),_CommunityTrap_Type())
communityTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:communityTrap.setStatus(_A)
_CommunityIPAddr_Type=IpAddress
_CommunityIPAddr_Object=MibTableColumn
communityIPAddr=_CommunityIPAddr_Object((1,3,6,1,4,1,52,1,52,2,1,3),_CommunityIPAddr_Type())
communityIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:communityIPAddr.setStatus(_A)
_CommunityIndex_Type=Integer32
_CommunityIndex_Object=MibTableColumn
communityIndex=_CommunityIndex_Object((1,3,6,1,4,1,52,1,52,2,1,4),_CommunityIndex_Type())
communityIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:communityIndex.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cabletron':cabletron,'commsDevice':commsDevice,'community':community,'communityTable':communityTable,'communityEntry':communityEntry,'communityName':communityName,'communityTrap':communityTrap,'communityIPAddr':communityIPAddr,_E:communityIndex})