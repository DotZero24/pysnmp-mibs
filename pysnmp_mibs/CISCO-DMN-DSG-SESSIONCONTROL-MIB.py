_F='read-only'
_E='read-write'
_D='writeOnly'
_C='DisplayString'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
ciscoDSGSessionControl=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,6))
if mibBuilder.loadTexts:ciscoDSGSessionControl.setRevisions(('2010-08-30 11:00','2009-11-22 15:00'))
class _SessionControlOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),(_D,2)))
_SessionControlOpen_Type.__name__=_A
_SessionControlOpen_Object=MibScalar
sessionControlOpen=_SessionControlOpen_Object((1,3,6,1,4,1,1429,2,2,5,6,1),_SessionControlOpen_Type())
sessionControlOpen.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionControlOpen.setStatus(_B)
class _SessionControlClose_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('saveAndClose',1),('ignoreAndClose',2),(_D,3)))
_SessionControlClose_Type.__name__=_A
_SessionControlClose_Object=MibScalar
sessionControlClose=_SessionControlClose_Object((1,3,6,1,4,1,1429,2,2,5,6,2),_SessionControlClose_Type())
sessionControlClose.setMaxAccess(_E)
if mibBuilder.loadTexts:sessionControlClose.setStatus(_B)
class _SessionControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('open',1),('closed',2),('expired',3),('openWithInvalidConfig',4)))
_SessionControlStatus_Type.__name__=_A
_SessionControlStatus_Object=MibScalar
sessionControlStatus=_SessionControlStatus_Object((1,3,6,1,4,1,1429,2,2,5,6,3),_SessionControlStatus_Type())
sessionControlStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:sessionControlStatus.setStatus(_B)
class _SessionControlValidateStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_SessionControlValidateStatus_Type.__name__=_C
_SessionControlValidateStatus_Object=MibScalar
sessionControlValidateStatus=_SessionControlValidateStatus_Object((1,3,6,1,4,1,1429,2,2,5,6,4),_SessionControlValidateStatus_Type())
sessionControlValidateStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:sessionControlValidateStatus.setStatus(_B)
mibBuilder.exportSymbols('CISCO-DMN-DSG-SESSIONCONTROL-MIB',**{'ciscoDSGSessionControl':ciscoDSGSessionControl,'sessionControlOpen':sessionControlOpen,'sessionControlClose':sessionControlClose,'sessionControlStatus':sessionControlStatus,'sessionControlValidateStatus':sessionControlValidateStatus})