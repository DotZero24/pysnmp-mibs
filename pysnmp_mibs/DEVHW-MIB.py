_C='DisplayString'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
aniDevHardware=ModuleIdentity((1,3,6,1,4,1,4325,2,3))
_AniDevHwRevision_Type=Integer32
_AniDevHwRevision_Object=MibScalar
aniDevHwRevision=_AniDevHwRevision_Object((1,3,6,1,4,1,4325,2,3,1),_AniDevHwRevision_Type())
aniDevHwRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevHwRevision.setStatus(_B)
_AniDevHwSpeed_Type=DisplayString
_AniDevHwSpeed_Object=MibScalar
aniDevHwSpeed=_AniDevHwSpeed_Object((1,3,6,1,4,1,4325,2,3,2),_AniDevHwSpeed_Type())
aniDevHwSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevHwSpeed.setStatus(_B)
class _AniDevHwBuildDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_AniDevHwBuildDate_Type.__name__=_C
_AniDevHwBuildDate_Object=MibScalar
aniDevHwBuildDate=_AniDevHwBuildDate_Object((1,3,6,1,4,1,4325,2,3,3),_AniDevHwBuildDate_Type())
aniDevHwBuildDate.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevHwBuildDate.setStatus(_B)
class _AniDevHwSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AniDevHwSerialNum_Type.__name__=_C
_AniDevHwSerialNum_Object=MibScalar
aniDevHwSerialNum=_AniDevHwSerialNum_Object((1,3,6,1,4,1,4325,2,3,4),_AniDevHwSerialNum_Type())
aniDevHwSerialNum.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevHwSerialNum.setStatus(_B)
_AniDevHwBoardRevision_Type=Integer32
_AniDevHwBoardRevision_Object=MibScalar
aniDevHwBoardRevision=_AniDevHwBoardRevision_Object((1,3,6,1,4,1,4325,2,3,5),_AniDevHwBoardRevision_Type())
aniDevHwBoardRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevHwBoardRevision.setStatus(_B)
mibBuilder.exportSymbols('DEVHW-MIB',**{'aniDevHardware':aniDevHardware,'aniDevHwRevision':aniDevHwRevision,'aniDevHwSpeed':aniDevHwSpeed,'aniDevHwBuildDate':aniDevHwBuildDate,'aniDevHwSerialNum':aniDevHwSerialNum,'aniDevHwBoardRevision':aniDevHwBoardRevision})