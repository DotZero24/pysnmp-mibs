_D='not-applicable'
_C='read-only'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aniDevEthernet=ModuleIdentity((1,3,6,1,4,1,4325,2,11))
_AniDevEthernetConfig_ObjectIdentity=ObjectIdentity
aniDevEthernetConfig=_AniDevEthernetConfig_ObjectIdentity((1,3,6,1,4,1,4325,2,11,1))
class _AniDevEthernetConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('auto-negotiate',1),('speed-100mbps-full',2),('speed-100mbps-half',3),('speed-10mbps-full',4),('speed-10mbps-half',5)))
_AniDevEthernetConfigMode_Type.__name__=_A
_AniDevEthernetConfigMode_Object=MibScalar
aniDevEthernetConfigMode=_AniDevEthernetConfigMode_Object((1,3,6,1,4,1,4325,2,11,1,1),_AniDevEthernetConfigMode_Type())
aniDevEthernetConfigMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:aniDevEthernetConfigMode.setStatus(_B)
class _AniDevEthernetCurrentLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AniDevEthernetCurrentLinkStatus_Type.__name__=_A
_AniDevEthernetCurrentLinkStatus_Object=MibScalar
aniDevEthernetCurrentLinkStatus=_AniDevEthernetCurrentLinkStatus_Object((1,3,6,1,4,1,4325,2,11,1,2),_AniDevEthernetCurrentLinkStatus_Type())
aniDevEthernetCurrentLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevEthernetCurrentLinkStatus.setStatus(_B)
class _AniDevEthernetCurrentSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('speed-10-mbps',1),('speed-100-mbps',2),(_D,3)))
_AniDevEthernetCurrentSpeed_Type.__name__=_A
_AniDevEthernetCurrentSpeed_Object=MibScalar
aniDevEthernetCurrentSpeed=_AniDevEthernetCurrentSpeed_Object((1,3,6,1,4,1,4325,2,11,1,3),_AniDevEthernetCurrentSpeed_Type())
aniDevEthernetCurrentSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevEthernetCurrentSpeed.setStatus(_B)
class _AniDevEthernetCurrentDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('half-duplex',1),('full-duplex',2),(_D,3)))
_AniDevEthernetCurrentDuplex_Type.__name__=_A
_AniDevEthernetCurrentDuplex_Object=MibScalar
aniDevEthernetCurrentDuplex=_AniDevEthernetCurrentDuplex_Object((1,3,6,1,4,1,4325,2,11,1,4),_AniDevEthernetCurrentDuplex_Type())
aniDevEthernetCurrentDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevEthernetCurrentDuplex.setStatus(_B)
mibBuilder.exportSymbols('DEVETHERNET-MIB',**{'aniDevEthernet':aniDevEthernet,'aniDevEthernetConfig':aniDevEthernetConfig,'aniDevEthernetConfigMode':aniDevEthernetConfigMode,'aniDevEthernetCurrentLinkStatus':aniDevEthernetCurrentLinkStatus,'aniDevEthernetCurrentSpeed':aniDevEthernetCurrentSpeed,'aniDevEthernetCurrentDuplex':aniDevEthernetCurrentDuplex})