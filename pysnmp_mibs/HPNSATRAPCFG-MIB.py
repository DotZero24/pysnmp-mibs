_H='read-write'
_G='hpnsaTrapCfgAgentIndex'
_F='HPNSATRAPCFG-MIB'
_E='OctetString'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaTrapCfg_ObjectIdentity=ObjectIdentity
hpnsaTrapCfg=_HpnsaTrapCfg_ObjectIdentity((1,3,6,1,4,1,11,2,23,13))
_HpnsaTrapCfgMibRev_ObjectIdentity=ObjectIdentity
hpnsaTrapCfgMibRev=_HpnsaTrapCfgMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,13,1))
class _HpnsaTrapCfgMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaTrapCfgMibRevMajor_Type.__name__=_C
_HpnsaTrapCfgMibRevMajor_Object=MibScalar
hpnsaTrapCfgMibRevMajor=_HpnsaTrapCfgMibRevMajor_Object((1,3,6,1,4,1,11,2,23,13,1,1),_HpnsaTrapCfgMibRevMajor_Type())
hpnsaTrapCfgMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapCfgMibRevMajor.setStatus(_A)
class _HpnsaTrapCfgMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaTrapCfgMibRevMinor_Type.__name__=_C
_HpnsaTrapCfgMibRevMinor_Object=MibScalar
hpnsaTrapCfgMibRevMinor=_HpnsaTrapCfgMibRevMinor_Object((1,3,6,1,4,1,11,2,23,13,1,2),_HpnsaTrapCfgMibRevMinor_Type())
hpnsaTrapCfgMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapCfgMibRevMinor.setStatus(_A)
_HpnsaTrapCfgAgent_ObjectIdentity=ObjectIdentity
hpnsaTrapCfgAgent=_HpnsaTrapCfgAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,13,2))
_HpnsaTrapCfgAgentTable_Object=MibTable
hpnsaTrapCfgAgentTable=_HpnsaTrapCfgAgentTable_Object((1,3,6,1,4,1,11,2,23,13,2,1))
if mibBuilder.loadTexts:hpnsaTrapCfgAgentTable.setStatus(_A)
_HpnsaTrapCfgAgentEntry_Object=MibTableRow
hpnsaTrapCfgAgentEntry=_HpnsaTrapCfgAgentEntry_Object((1,3,6,1,4,1,11,2,23,13,2,1,1))
hpnsaTrapCfgAgentEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnsaTrapCfgAgentEntry.setStatus(_A)
class _HpnsaTrapCfgAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaTrapCfgAgentIndex_Type.__name__=_C
_HpnsaTrapCfgAgentIndex_Object=MibTableColumn
hpnsaTrapCfgAgentIndex=_HpnsaTrapCfgAgentIndex_Object((1,3,6,1,4,1,11,2,23,13,2,1,1,1),_HpnsaTrapCfgAgentIndex_Type())
hpnsaTrapCfgAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapCfgAgentIndex.setStatus(_A)
class _HpnsaTrapCfgAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaTrapCfgAgentName_Type.__name__=_D
_HpnsaTrapCfgAgentName_Object=MibTableColumn
hpnsaTrapCfgAgentName=_HpnsaTrapCfgAgentName_Object((1,3,6,1,4,1,11,2,23,13,2,1,1,2),_HpnsaTrapCfgAgentName_Type())
hpnsaTrapCfgAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapCfgAgentName.setStatus(_A)
class _HpnsaTrapCfgAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnsaTrapCfgAgentVersion_Type.__name__=_D
_HpnsaTrapCfgAgentVersion_Object=MibTableColumn
hpnsaTrapCfgAgentVersion=_HpnsaTrapCfgAgentVersion_Object((1,3,6,1,4,1,11,2,23,13,2,1,1,3),_HpnsaTrapCfgAgentVersion_Type())
hpnsaTrapCfgAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapCfgAgentVersion.setStatus(_A)
class _HpnsaTrapCfgAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_HpnsaTrapCfgAgentDate_Type.__name__=_E
_HpnsaTrapCfgAgentDate_Object=MibTableColumn
hpnsaTrapCfgAgentDate=_HpnsaTrapCfgAgentDate_Object((1,3,6,1,4,1,11,2,23,13,2,1,1,4),_HpnsaTrapCfgAgentDate_Type())
hpnsaTrapCfgAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapCfgAgentDate.setStatus(_A)
_HpnsaTrapTargetCfg_ObjectIdentity=ObjectIdentity
hpnsaTrapTargetCfg=_HpnsaTrapTargetCfg_ObjectIdentity((1,3,6,1,4,1,11,2,23,13,3))
class _HpnsaRemoveTrapTarget_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_HpnsaRemoveTrapTarget_Type.__name__=_D
_HpnsaRemoveTrapTarget_Object=MibScalar
hpnsaRemoveTrapTarget=_HpnsaRemoveTrapTarget_Object((1,3,6,1,4,1,11,2,23,13,3,1),_HpnsaRemoveTrapTarget_Type())
hpnsaRemoveTrapTarget.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnsaRemoveTrapTarget.setStatus(_A)
class _HpnsaAddTrapTarget_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_HpnsaAddTrapTarget_Type.__name__=_D
_HpnsaAddTrapTarget_Object=MibScalar
hpnsaAddTrapTarget=_HpnsaAddTrapTarget_Object((1,3,6,1,4,1,11,2,23,13,3,2),_HpnsaAddTrapTarget_Type())
hpnsaAddTrapTarget.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnsaAddTrapTarget.setStatus(_A)
class _HpnsaRestartSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noActionNeeded',1),('restartSNMP',2)))
_HpnsaRestartSNMP_Type.__name__=_C
_HpnsaRestartSNMP_Object=MibScalar
hpnsaRestartSNMP=_HpnsaRestartSNMP_Object((1,3,6,1,4,1,11,2,23,13,3,3),_HpnsaRestartSNMP_Type())
hpnsaRestartSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRestartSNMP.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaTrapCfg':hpnsaTrapCfg,'hpnsaTrapCfgMibRev':hpnsaTrapCfgMibRev,'hpnsaTrapCfgMibRevMajor':hpnsaTrapCfgMibRevMajor,'hpnsaTrapCfgMibRevMinor':hpnsaTrapCfgMibRevMinor,'hpnsaTrapCfgAgent':hpnsaTrapCfgAgent,'hpnsaTrapCfgAgentTable':hpnsaTrapCfgAgentTable,'hpnsaTrapCfgAgentEntry':hpnsaTrapCfgAgentEntry,_G:hpnsaTrapCfgAgentIndex,'hpnsaTrapCfgAgentName':hpnsaTrapCfgAgentName,'hpnsaTrapCfgAgentVersion':hpnsaTrapCfgAgentVersion,'hpnsaTrapCfgAgentDate':hpnsaTrapCfgAgentDate,'hpnsaTrapTargetCfg':hpnsaTrapTargetCfg,'hpnsaRemoveTrapTarget':hpnsaRemoveTrapTarget,'hpnsaAddTrapTarget':hpnsaAddTrapTarget,'hpnsaRestartSNMP':hpnsaRestartSNMP})