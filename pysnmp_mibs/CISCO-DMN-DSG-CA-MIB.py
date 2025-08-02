_F='caIndex'
_E='CISCO-DMN-DSG-CA-MIB'
_D='Integer32'
_C='read-only'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
ciscoDSGCA=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,11))
if mibBuilder.loadTexts:ciscoDSGCA.setRevisions(('2010-08-30 05:00','2010-06-17 06:00','2010-03-22 05:00','2010-02-12 12:00','2009-12-07 12:00'))
_Ca_ObjectIdentity=ObjectIdentity
ca=_Ca_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,11,1))
class _CaClearADP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('writeOnly',1),('yes',2)))
_CaClearADP_Type.__name__=_D
_CaClearADP_Object=MibScalar
caClearADP=_CaClearADP_Object((1,3,6,1,4,1,1429,2,2,5,11,1,1),_CaClearADP_Type())
caClearADP.setMaxAccess('read-write')
if mibBuilder.loadTexts:caClearADP.setStatus(_A)
_CaTable_ObjectIdentity=ObjectIdentity
caTable=_CaTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,11,2))
_CaADPTable_Object=MibTable
caADPTable=_CaADPTable_Object((1,3,6,1,4,1,1429,2,2,5,11,2,1))
if mibBuilder.loadTexts:caADPTable.setStatus(_A)
_CaADPEntry_Object=MibTableRow
caADPEntry=_CaADPEntry_Object((1,3,6,1,4,1,1429,2,2,5,11,2,1,1))
caADPEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:caADPEntry.setStatus(_A)
class _CaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CaIndex_Type.__name__=_D
_CaIndex_Object=MibTableColumn
caIndex=_CaIndex_Object((1,3,6,1,4,1,1429,2,2,5,11,2,1,1,1),_CaIndex_Type())
caIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:caIndex.setStatus(_A)
class _CaUsrAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CaUsrAddr_Type.__name__=_B
_CaUsrAddr_Object=MibTableColumn
caUsrAddr=_CaUsrAddr_Object((1,3,6,1,4,1,1429,2,2,5,11,2,1,1,2),_CaUsrAddr_Type())
caUsrAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:caUsrAddr.setStatus(_A)
class _CaISEVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CaISEVer_Type.__name__=_B
_CaISEVer_Object=MibTableColumn
caISEVer=_CaISEVer_Object((1,3,6,1,4,1,1429,2,2,5,11,2,1,1,3),_CaISEVer_Type())
caISEVer.setMaxAccess(_C)
if mibBuilder.loadTexts:caISEVer.setStatus(_A)
class _CaADPEncPass_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CaADPEncPass_Type.__name__=_B
_CaADPEncPass_Object=MibTableColumn
caADPEncPass=_CaADPEncPass_Object((1,3,6,1,4,1,1429,2,2,5,11,2,1,1,4),_CaADPEncPass_Type())
caADPEncPass.setMaxAccess(_C)
if mibBuilder.loadTexts:caADPEncPass.setStatus(_A)
class _CaADPEncTotal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CaADPEncTotal_Type.__name__=_B
_CaADPEncTotal_Object=MibTableColumn
caADPEncTotal=_CaADPEncTotal_Object((1,3,6,1,4,1,1429,2,2,5,11,2,1,1,5),_CaADPEncTotal_Type())
caADPEncTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:caADPEncTotal.setStatus(_A)
class _CaADPNonEncPass_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CaADPNonEncPass_Type.__name__=_B
_CaADPNonEncPass_Object=MibTableColumn
caADPNonEncPass=_CaADPNonEncPass_Object((1,3,6,1,4,1,1429,2,2,5,11,2,1,1,6),_CaADPNonEncPass_Type())
caADPNonEncPass.setMaxAccess(_C)
if mibBuilder.loadTexts:caADPNonEncPass.setStatus(_A)
class _CaADPNonEncTotal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CaADPNonEncTotal_Type.__name__=_B
_CaADPNonEncTotal_Object=MibTableColumn
caADPNonEncTotal=_CaADPNonEncTotal_Object((1,3,6,1,4,1,1429,2,2,5,11,2,1,1,7),_CaADPNonEncTotal_Type())
caADPNonEncTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:caADPNonEncTotal.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGCA':ciscoDSGCA,'ca':ca,'caClearADP':caClearADP,'caTable':caTable,'caADPTable':caADPTable,'caADPEntry':caADPEntry,_F:caIndex,'caUsrAddr':caUsrAddr,'caISEVer':caISEVer,'caADPEncPass':caADPEncPass,'caADPEncTotal':caADPEncTotal,'caADPNonEncPass':caADPNonEncPass,'caADPNonEncTotal':caADPNonEncTotal})