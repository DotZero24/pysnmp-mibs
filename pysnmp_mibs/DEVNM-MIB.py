_F='aniDevNMAccessIndex'
_E='DEVNM-MIB'
_D='DisplayString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
aniDevNetworkManager=ModuleIdentity((1,3,6,1,4,1,4325,2,7))
class _AniDevNumManagingHosts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AniDevNumManagingHosts_Type.__name__=_B
_AniDevNumManagingHosts_Object=MibScalar
aniDevNumManagingHosts=_AniDevNumManagingHosts_Object((1,3,6,1,4,1,4325,2,7,1),_AniDevNumManagingHosts_Type())
aniDevNumManagingHosts.setMaxAccess('read-only')
if mibBuilder.loadTexts:aniDevNumManagingHosts.setStatus(_A)
_AniDevNetworkMgrAccessTable_Object=MibTable
aniDevNetworkMgrAccessTable=_AniDevNetworkMgrAccessTable_Object((1,3,6,1,4,1,4325,2,7,2))
if mibBuilder.loadTexts:aniDevNetworkMgrAccessTable.setStatus(_A)
_AniDevNetworkMgrAccessEntry_Object=MibTableRow
aniDevNetworkMgrAccessEntry=_AniDevNetworkMgrAccessEntry_Object((1,3,6,1,4,1,4325,2,7,2,1))
aniDevNetworkMgrAccessEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aniDevNetworkMgrAccessEntry.setStatus(_A)
class _AniDevNMAccessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AniDevNMAccessIndex_Type.__name__=_B
_AniDevNMAccessIndex_Object=MibTableColumn
aniDevNMAccessIndex=_AniDevNMAccessIndex_Object((1,3,6,1,4,1,4325,2,7,2,1,1),_AniDevNMAccessIndex_Type())
aniDevNMAccessIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:aniDevNMAccessIndex.setStatus(_A)
_AniDevNMAccessIp_Type=IpAddress
_AniDevNMAccessIp_Object=MibTableColumn
aniDevNMAccessIp=_AniDevNMAccessIp_Object((1,3,6,1,4,1,4325,2,7,2,1,2),_AniDevNMAccessIp_Type())
aniDevNMAccessIp.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevNMAccessIp.setStatus(_A)
class _AniDevNMReadAccessCommunity_Type(DisplayString):defaultValue=OctetString('public');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AniDevNMReadAccessCommunity_Type.__name__=_D
_AniDevNMReadAccessCommunity_Object=MibTableColumn
aniDevNMReadAccessCommunity=_AniDevNMReadAccessCommunity_Object((1,3,6,1,4,1,4325,2,7,2,1,3),_AniDevNMReadAccessCommunity_Type())
aniDevNMReadAccessCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevNMReadAccessCommunity.setStatus(_A)
class _AniDevNMWriteAccessCommunity_Type(DisplayString):defaultValue=OctetString('private');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AniDevNMWriteAccessCommunity_Type.__name__=_D
_AniDevNMWriteAccessCommunity_Object=MibTableColumn
aniDevNMWriteAccessCommunity=_AniDevNMWriteAccessCommunity_Object((1,3,6,1,4,1,4325,2,7,2,1,4),_AniDevNMWriteAccessCommunity_Type())
aniDevNMWriteAccessCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevNMWriteAccessCommunity.setStatus(_A)
class _AniDevNMAccessControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('read',1),('readWrite',2),('roWithTraps',3),('rwWithTraps',4),('trapsOnly',5)))
_AniDevNMAccessControl_Type.__name__=_B
_AniDevNMAccessControl_Object=MibTableColumn
aniDevNMAccessControl=_AniDevNMAccessControl_Object((1,3,6,1,4,1,4325,2,7,2,1,5),_AniDevNMAccessControl_Type())
aniDevNMAccessControl.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevNMAccessControl.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'aniDevNetworkManager':aniDevNetworkManager,'aniDevNumManagingHosts':aniDevNumManagingHosts,'aniDevNetworkMgrAccessTable':aniDevNetworkMgrAccessTable,'aniDevNetworkMgrAccessEntry':aniDevNetworkMgrAccessEntry,_F:aniDevNMAccessIndex,'aniDevNMAccessIp':aniDevNMAccessIp,'aniDevNMReadAccessCommunity':aniDevNMReadAccessCommunity,'aniDevNMWriteAccessCommunity':aniDevNMWriteAccessCommunity,'aniDevNMAccessControl':aniDevNMAccessControl})