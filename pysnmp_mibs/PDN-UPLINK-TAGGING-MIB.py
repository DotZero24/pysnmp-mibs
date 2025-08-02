_U='ultIndex'
_T='ultBaseVlanTag'
_S='pdn24UltBaseVlanTag'
_R='pdn48UltBaseVlanTag'
_Q='Unsigned32'
_P='VlanId'
_O='pdnGenUltBaseVlanTag'
_N='pdnUltIndex'
_M='deprecated'
_L='ultBase3584'
_K='ultBase3072'
_J='ultBase2560'
_I='ultBase2048'
_H='ultBase1536'
_G='ultBase1024'
_F='ultBase512'
_E='ultBase16'
_D='Integer32'
_C='current'
_B='read-write'
_A='PDN-UPLINK-TAGGING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnUplinkTagging=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,37))
if mibBuilder.loadTexts:pdnUplinkTagging.setRevisions(('2003-03-12 00:00','2002-05-15 00:00'))
_PdnUplinkTaggingObjects_ObjectIdentity=ObjectIdentity
pdnUplinkTaggingObjects=_PdnUplinkTaggingObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,37,1))
class _UltBaseVlanTag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7),(_L,8)))
_UltBaseVlanTag_Type.__name__=_D
_UltBaseVlanTag_Object=MibScalar
ultBaseVlanTag=_UltBaseVlanTag_Object((1,3,6,1,4,1,1795,2,24,2,37,1,1),_UltBaseVlanTag_Type())
ultBaseVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:ultBaseVlanTag.setStatus(_M)
class _UltIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_UltIndex_Type.__name__=_D
_UltIndex_Object=MibScalar
ultIndex=_UltIndex_Object((1,3,6,1,4,1,1795,2,24,2,37,1,2),_UltIndex_Type())
ultIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ultIndex.setStatus(_M)
_PdnUplinkTaggingConformance_ObjectIdentity=ObjectIdentity
pdnUplinkTaggingConformance=_PdnUplinkTaggingConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,37,2))
_PdnUplinkTaggingGroups_ObjectIdentity=ObjectIdentity
pdnUplinkTaggingGroups=_PdnUplinkTaggingGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,37,2,1))
_PdnUplinkTaggingCompliances_ObjectIdentity=ObjectIdentity
pdnUplinkTaggingCompliances=_PdnUplinkTaggingCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,37,2,2))
_PdnUplinkTaggingDeprecatedGroup_ObjectIdentity=ObjectIdentity
pdnUplinkTaggingDeprecatedGroup=_PdnUplinkTaggingDeprecatedGroup_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,37,2,3))
_PdnUplinkTaggingObjectsR2_ObjectIdentity=ObjectIdentity
pdnUplinkTaggingObjectsR2=_PdnUplinkTaggingObjectsR2_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,37,3))
class _PdnUltIndex_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_PdnUltIndex_Type.__name__=_Q
_PdnUltIndex_Object=MibScalar
pdnUltIndex=_PdnUltIndex_Object((1,3,6,1,4,1,1795,2,24,2,37,3,1),_PdnUltIndex_Type())
pdnUltIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnUltIndex.setStatus(_C)
class _PdnGenUltBaseVlanTag_Type(VlanId):defaultValue=16
_PdnGenUltBaseVlanTag_Type.__name__=_P
_PdnGenUltBaseVlanTag_Object=MibScalar
pdnGenUltBaseVlanTag=_PdnGenUltBaseVlanTag_Object((1,3,6,1,4,1,1795,2,24,2,37,3,2),_PdnGenUltBaseVlanTag_Type())
pdnGenUltBaseVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnGenUltBaseVlanTag.setStatus(_C)
class _Pdn48UltBaseVlanTag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7),(_L,8)))
_Pdn48UltBaseVlanTag_Type.__name__=_D
_Pdn48UltBaseVlanTag_Object=MibScalar
pdn48UltBaseVlanTag=_Pdn48UltBaseVlanTag_Object((1,3,6,1,4,1,1795,2,24,2,37,3,3),_Pdn48UltBaseVlanTag_Type())
pdn48UltBaseVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:pdn48UltBaseVlanTag.setStatus(_C)
class _Pdn24UltBaseVlanTag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_E,1),('ultBase256',2),(_F,3),('ultBase768',4),(_G,5),('ultBase1280',6),(_H,7),('ultBase1792',8),(_I,9),('ultBase2304',10),(_J,11),('ultBase2816',12),(_K,13),('ultBase3328',14),(_L,15),('ultBase3840',16)))
_Pdn24UltBaseVlanTag_Type.__name__=_D
_Pdn24UltBaseVlanTag_Object=MibScalar
pdn24UltBaseVlanTag=_Pdn24UltBaseVlanTag_Object((1,3,6,1,4,1,1795,2,24,2,37,3,4),_Pdn24UltBaseVlanTag_Type())
pdn24UltBaseVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:pdn24UltBaseVlanTag.setStatus(_C)
pdn48PortUpLinkTaggingGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,37,2,1,1))
pdn48PortUpLinkTaggingGroup.setObjects(*((_A,_N),(_A,_O),(_A,_R)))
if mibBuilder.loadTexts:pdn48PortUpLinkTaggingGroup.setStatus(_C)
pdn24PortUpLinkTaggingGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,37,2,1,2))
pdn24PortUpLinkTaggingGroup.setObjects(*((_A,_N),(_A,_O),(_A,_S)))
if mibBuilder.loadTexts:pdn24PortUpLinkTaggingGroup.setStatus(_C)
upLinkTaggingDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,37,2,3,1))
upLinkTaggingDeprecatedGroup.setObjects(*((_A,_T),(_A,_U)))
if mibBuilder.loadTexts:upLinkTaggingDeprecatedGroup.setStatus(_M)
mibBuilder.exportSymbols(_A,**{'pdnUplinkTagging':pdnUplinkTagging,'pdnUplinkTaggingObjects':pdnUplinkTaggingObjects,_T:ultBaseVlanTag,_U:ultIndex,'pdnUplinkTaggingConformance':pdnUplinkTaggingConformance,'pdnUplinkTaggingGroups':pdnUplinkTaggingGroups,'pdn48PortUpLinkTaggingGroup':pdn48PortUpLinkTaggingGroup,'pdn24PortUpLinkTaggingGroup':pdn24PortUpLinkTaggingGroup,'pdnUplinkTaggingCompliances':pdnUplinkTaggingCompliances,'pdnUplinkTaggingDeprecatedGroup':pdnUplinkTaggingDeprecatedGroup,'upLinkTaggingDeprecatedGroup':upLinkTaggingDeprecatedGroup,'pdnUplinkTaggingObjectsR2':pdnUplinkTaggingObjectsR2,_N:pdnUltIndex,_O:pdnGenUltBaseVlanTag,_R:pdn48UltBaseVlanTag,_S:pdn24UltBaseVlanTag})