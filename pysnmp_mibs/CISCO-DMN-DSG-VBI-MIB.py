_E='enable'
_D='disable'
_C='read-write'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDSGVBI=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,31))
if mibBuilder.loadTexts:ciscoDSGVBI.setRevisions(('2012-03-20 10:00','2010-07-26 10:00'))
class _VbiVitsFlag17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_VbiVitsFlag17_Type.__name__=_A
_VbiVitsFlag17_Object=MibScalar
vbiVitsFlag17=_VbiVitsFlag17_Object((1,3,6,1,4,1,1429,2,2,5,31,1),_VbiVitsFlag17_Type())
vbiVitsFlag17.setMaxAccess(_C)
if mibBuilder.loadTexts:vbiVitsFlag17.setStatus(_B)
class _VbiVitsFlag18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_VbiVitsFlag18_Type.__name__=_A
_VbiVitsFlag18_Object=MibScalar
vbiVitsFlag18=_VbiVitsFlag18_Object((1,3,6,1,4,1,1429,2,2,5,31,2),_VbiVitsFlag18_Type())
vbiVitsFlag18.setMaxAccess(_C)
if mibBuilder.loadTexts:vbiVitsFlag18.setStatus(_B)
class _VbiVitsFlag330_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_VbiVitsFlag330_Type.__name__=_A
_VbiVitsFlag330_Object=MibScalar
vbiVitsFlag330=_VbiVitsFlag330_Object((1,3,6,1,4,1,1429,2,2,5,31,3),_VbiVitsFlag330_Type())
vbiVitsFlag330.setMaxAccess(_C)
if mibBuilder.loadTexts:vbiVitsFlag330.setStatus(_B)
class _VbiVitsFlag331_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_VbiVitsFlag331_Type.__name__=_A
_VbiVitsFlag331_Object=MibScalar
vbiVitsFlag331=_VbiVitsFlag331_Object((1,3,6,1,4,1,1429,2,2,5,31,4),_VbiVitsFlag331_Type())
vbiVitsFlag331.setMaxAccess(_C)
if mibBuilder.loadTexts:vbiVitsFlag331.setStatus(_B)
class _VbiVitcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('passthrough',1),('suppress',2),('autoGenerate',3)))
_VbiVitcMode_Type.__name__=_A
_VbiVitcMode_Object=MibScalar
vbiVitcMode=_VbiVitcMode_Object((1,3,6,1,4,1,1429,2,2,5,31,5),_VbiVitcMode_Type())
vbiVitcMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vbiVitcMode.setStatus(_B)
class _VbiTimeCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ltc',1),('vitc',2),('both',3)))
_VbiTimeCode_Type.__name__=_A
_VbiTimeCode_Object=MibScalar
vbiTimeCode=_VbiTimeCode_Object((1,3,6,1,4,1,1429,2,2,5,31,6),_VbiTimeCode_Type())
vbiTimeCode.setMaxAccess(_C)
if mibBuilder.loadTexts:vbiTimeCode.setStatus(_B)
class _VbiColorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_VbiColorMode_Type.__name__=_A
_VbiColorMode_Object=MibScalar
vbiColorMode=_VbiColorMode_Object((1,3,6,1,4,1,1429,2,2,5,31,7),_VbiColorMode_Type())
vbiColorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vbiColorMode.setStatus(_B)
class _VbiDelayComp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_VbiDelayComp_Type.__name__=_A
_VbiDelayComp_Object=MibScalar
vbiDelayComp=_VbiDelayComp_Object((1,3,6,1,4,1,1429,2,2,5,31,8),_VbiDelayComp_Type())
vbiDelayComp.setMaxAccess(_C)
if mibBuilder.loadTexts:vbiDelayComp.setStatus(_B)
class _VbiDropFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_VbiDropFrame_Type.__name__=_A
_VbiDropFrame_Object=MibScalar
vbiDropFrame=_VbiDropFrame_Object((1,3,6,1,4,1,1429,2,2,5,31,9),_VbiDropFrame_Type())
vbiDropFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:vbiDropFrame.setStatus(_B)
class _VbiVitcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ltc',1),('vitc',2),('both',3),('undefined',4)))
_VbiVitcStatus_Type.__name__=_A
_VbiVitcStatus_Object=MibScalar
vbiVitcStatus=_VbiVitcStatus_Object((1,3,6,1,4,1,1429,2,2,5,31,10),_VbiVitcStatus_Type())
vbiVitcStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:vbiVitcStatus.setStatus(_B)
mibBuilder.exportSymbols('CISCO-DMN-DSG-VBI-MIB',**{'ciscoDSGVBI':ciscoDSGVBI,'vbiVitsFlag17':vbiVitsFlag17,'vbiVitsFlag18':vbiVitsFlag18,'vbiVitsFlag330':vbiVitsFlag330,'vbiVitsFlag331':vbiVitsFlag331,'vbiVitcMode':vbiVitcMode,'vbiTimeCode':vbiTimeCode,'vbiColorMode':vbiColorMode,'vbiDelayComp':vbiDelayComp,'vbiDropFrame':vbiDropFrame,'vbiVitcStatus':vbiVitcStatus})