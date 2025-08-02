_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyACS5KMgmt,=mibBuilder.importSymbols('CYCLADES-ACS5K-MIB','cyACS5KMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cyACS5KAdm=ModuleIdentity((1,3,6,1,4,1,2925,8,4))
if mibBuilder.loadTexts:cyACS5KAdm.setRevisions(('2010-07-26 00:00',))
class _CyACS5KSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nosave',0),('save',1)))
_CyACS5KSave_Type.__name__=_A
_CyACS5KSave_Object=MibScalar
cyACS5KSave=_CyACS5KSave_Object((1,3,6,1,4,1,2925,8,4,1),_CyACS5KSave_Type())
cyACS5KSave.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KSave.setStatus(_C)
class _CyACS5KSerialHUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('norestartportslave',0),('restartportslave',1)))
_CyACS5KSerialHUP_Type.__name__=_A
_CyACS5KSerialHUP_Object=MibScalar
cyACS5KSerialHUP=_CyACS5KSerialHUP_Object((1,3,6,1,4,1,2925,8,4,2),_CyACS5KSerialHUP_Type())
cyACS5KSerialHUP.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KSerialHUP.setStatus(_C)
mibBuilder.exportSymbols('CYCLADES-ACS5K-ADM-MIB',**{'cyACS5KAdm':cyACS5KAdm,'cyACS5KSave':cyACS5KSave,'cyACS5KSerialHUP':cyACS5KSerialHUP})